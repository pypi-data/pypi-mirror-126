
import time
import argparse
from collections import deque
from dashing import VSplit, HSplit, HGauge, HChart
from .utils import *


parser = argparse.ArgumentParser(description='asitop: Performance monitoring CLI tool for Apple Silicon')
parser.add_argument('--interval', type=int, default=1,
                    help='Display interval and sampling interval for powermetrics (seconds)')
parser.add_argument('--color', type=int, default=2,
                    help='Choose display color (0~8)')
parser.add_argument('--avg', type=int, default=30,
                    help='Interval for averaged values (seconds)')
args = parser.parse_args()


def main():
    print("\n[1/3] Loading ASITOP\n")

    ui = VSplit(
        VSplit(
            HSplit(
                HGauge(title="E-CPU Usage", val=0, color=args.color),
                HGauge(title="P-CPU Usage", val=0, color=args.color),
            ),
            HGauge(title="GPU Usage", val=0, color=args.color),
            title="Usage Gauge",
            border_color=args.color,
        ),
        VSplit(
            HGauge(title="RAM Usage", val=0, color=args.color),
            HSplit(
                HGauge(title="E-CPU B/W", val=50, color=args.color),
                HGauge(title="P-CPU B/W", val=50, color=args.color),
                HGauge(title="GPU B/W", val=50, color=args.color),
            ),
            border_color=args.color,
            title="Memory"
        ),
        HSplit(
            HChart(title="CPU Power", color=args.color),
            HChart(title="GPU Power", color=args.color),
            title="Power Chart",
            border_color=args.color,
        ),
    )

    usage_gauges = ui.items[0]
    memory_gauges = ui.items[1]
    power_charts = ui.items[2]

    cpu_gauges = usage_gauges.items[0]
    cpu1_gauge = cpu_gauges.items[0]
    cpu2_gauge = cpu_gauges.items[1]
    gpu_gauge = usage_gauges.items[1]

    ram_gauge = memory_gauges.items[0]

    bw_gauges = memory_gauges.items[1]
    ecpu_bw_gauge = bw_gauges.items[0]
    pcpu_bw_gauge = bw_gauges.items[1]
    gpu_bw_gauge = bw_gauges.items[2]

    cpu_power_chart = power_charts.items[0]
    gpu_power_chart = power_charts.items[1]

    cpu_info_dict = get_cpu_info()
    cpu_title = cpu_info_dict["machdep.cpu.brand_string"] + \
        " (" + cpu_info_dict["machdep.cpu.core_count"] + "-core)"
    if cpu_info_dict["machdep.cpu.brand_string"] == "Apple M1 Max" or cpu_info_dict["machdep.cpu.brand_string"] == "Apple M1 Pro":
        cpu_max_power = 30
        gpu_max_power = 60
    elif cpu_info_dict["machdep.cpu.brand_string"] == "Apple M1":
        cpu_max_power = 20
        gpu_max_power = 20
    if cpu_info_dict["machdep.cpu.brand_string"] == "Apple M1 Max":
        max_cpu_bw = 200
        max_gpu_bw = 400
    elif cpu_info_dict["machdep.cpu.brand_string"] == "Apple M1 Pro":
        max_cpu_bw = 200
        max_gpu_bw = 400
    elif cpu_info_dict["machdep.cpu.brand_string"] == "Apple M1":
        max_cpu_bw = 70
        max_gpu_bw = 70

    cpu_peak_power = 0
    gpu_peak_power = 0
    package_peak_power = 0

    print("\n[2/3] Starting powermetrics process\n")

    powermetrics_process = run_powermetrics_process(
        interval=args.interval*1000)

    print("\n[3/3] Waiting for first reading...\n")

    def get_reading(wait=0.1):
        ready = parse_powermetrics()
        while not ready:
            time.sleep(wait)
            ready = parse_powermetrics()
        return ready

    ready = get_reading()
    last_timestamp = ready[-1]

    usage_gauges.title = cpu_title

    def get_avg(inlist):
        avg = sum(inlist)/len(inlist)
        return avg

    avg_package_power_list = deque([], maxlen=int(args.avg/args.interval))
    avg_cpu_power_list = deque([], maxlen=int(args.avg/args.interval))
    avg_gpu_power_list = deque([], maxlen=int(args.avg/args.interval))

    clear_console()

    while True:
        try:
            ready = parse_powermetrics()
            if ready:
                cpu_metrics_dict, gpu_metrics_dict, thermal_pressure, bandwidth_metrics, timestamp = ready

                if timestamp > last_timestamp:
                    last_timestamp = timestamp

                    if thermal_pressure == "Nominal":
                        thermal_throttle = "no"
                    else:
                        thermal_throttle = "yes"

                    cpu1_gauge.title = "".join([
                        "E-CPU Usage: ",
                        str(cpu_metrics_dict["E-Cluster_active"]),
                        "% @ ",
                        str(cpu_metrics_dict["E-Cluster_freq_Mhz"]),
                        " MHz"
                    ])
                    cpu1_gauge.value = cpu_metrics_dict["E-Cluster_active"]

                    cpu2_gauge.title = "".join([
                        "P-CPU Usage: ",
                        str(cpu_metrics_dict["P-Cluster_active"]),
                        "% @ ",
                        str(cpu_metrics_dict["P-Cluster_freq_Mhz"]),
                        " MHz"
                    ])
                    cpu2_gauge.value = cpu_metrics_dict["P-Cluster_active"]

                    gpu_gauge.title = "".join([
                        "GPU Usage: ",
                        str(gpu_metrics_dict["active"]),
                        "% @ ",
                        str(gpu_metrics_dict["freq_MHz"]),
                        " MHz"
                    ])
                    gpu_gauge.value = gpu_metrics_dict["active"]

                    ram_metrics_dict = get_ram_metrics_dict()

                    if ram_metrics_dict["swap_total_GB"] < 0.1:
                        ram_gauge.title = "".join([
                            "RAM Usage: ",
                            str(ram_metrics_dict["used_GB"]),
                            "/",
                            str(ram_metrics_dict["total_GB"]),
                            "GB"
                        ])
                    else:
                        ram_gauge.title = "".join([
                            "RAM Usage: ",
                            str(ram_metrics_dict["used_GB"]),
                            "/",
                            str(ram_metrics_dict["total_GB"]),
                            "GB",
                            " - swap:",
                            str(ram_metrics_dict["swap_used_GB"]),
                            "/",
                            str(ram_metrics_dict["swap_total_GB"]),
                            "GB"
                        ])
                    ram_gauge.value = ram_metrics_dict["free_percent"]

                    ecpu_bw_percent = int(
                        (bandwidth_metrics["ECPU DCS RD"]+bandwidth_metrics["ECPU DCS WR"])/max_cpu_bw*100)
                    ecpu_read_GB = bandwidth_metrics["ECPU DCS RD"]
                    ecpu_write_GB = bandwidth_metrics["ECPU DCS WR"]
                    ecpu_bw_gauge.title = "".join([
                        "E-CPU R:",
                        '{0:.1f}'.format(ecpu_read_GB),
                        "/W:",
                        '{0:.1f}'.format(ecpu_write_GB),
                        " GB/s"
                    ])
                    ecpu_bw_gauge.value = ecpu_bw_percent

                    pcpu_bw_percent = int(
                        (bandwidth_metrics["PCPU DCS RD"]+bandwidth_metrics["PCPU DCS WR"])/max_cpu_bw*100)
                    pcpu_read_GB = bandwidth_metrics["PCPU DCS RD"]
                    pcpu_write_GB = bandwidth_metrics["PCPU DCS WR"]
                    pcpu_bw_gauge.title = "".join([
                        "P-CPU R:",
                        '{0:.1f}'.format(pcpu_read_GB),
                        "/W:",
                        '{0:.1f}'.format(pcpu_write_GB),
                        " GB/s"
                    ])
                    pcpu_bw_gauge.value = pcpu_bw_percent

                    gpu_bw_percent = int(
                        (bandwidth_metrics["GFX DCS RD"]+bandwidth_metrics["GFX DCS WR"])/max_gpu_bw*100)
                    gpu_read_GB = bandwidth_metrics["GFX DCS RD"]
                    gpu_write_GB = bandwidth_metrics["GFX DCS WR"]
                    gpu_bw_gauge.title = "".join([
                        "GPU R:",
                        '{0:.1f}'.format(gpu_read_GB),
                        "/W:",
                        '{0:.1f}'.format(gpu_write_GB),
                        " GB/s"
                    ])
                    gpu_bw_gauge.value = gpu_bw_percent

                    total_bw_GB = ecpu_read_GB+ecpu_write_GB+pcpu_read_GB+pcpu_write_GB+gpu_read_GB+gpu_write_GB
                    bw_gauges.title = "".join([
                        "Memory Bandwidth (GB/s) - total: ",
                        '{0:.2f}'.format(total_bw_GB),
                        " GB/s"
                    ])

                    package_power_W = cpu_metrics_dict["package_W"]
                    if package_power_W > package_peak_power:
                        package_peak_power = package_power_W
                    avg_package_power_list.append(package_power_W)
                    avg_package_power = get_avg(avg_package_power_list)
                    power_charts.title = "".join([
                        "Package Power: ",
                        '{0:.2f}'.format(package_power_W),
                        "W - avg: ",
                        '{0:.2f}'.format(avg_package_power),
                        "W - throttle: ",
                        thermal_throttle,
                    ])

                    cpu_power_percent = int(
                        cpu_metrics_dict["cpu_W"]/cpu_max_power*100)
                    cpu_power_W = cpu_metrics_dict["cpu_W"]
                    if cpu_power_W > cpu_peak_power:
                        cpu_peak_power = cpu_power_W
                    avg_cpu_power_list.append(cpu_power_W)
                    avg_cpu_power = get_avg(avg_cpu_power_list)
                    cpu_power_chart.title = "".join([
                        "CPU Power: ",
                        '{0:.2f}'.format(cpu_power_W),
                        "W - avg: ",
                        '{0:.2f}'.format(avg_cpu_power),
                        "W - peak: ",
                        '{0:.2f}'.format(cpu_peak_power),
                        "W"
                    ])
                    cpu_power_chart.append(cpu_power_percent)

                    gpu_power_percent = int(
                        cpu_metrics_dict["gpu_W"]/gpu_max_power*100)
                    gpu_power_W = cpu_metrics_dict["gpu_W"]
                    if gpu_power_W > gpu_peak_power:
                        gpu_peak_power = gpu_power_W
                    avg_gpu_power_list.append(gpu_power_W)
                    avg_gpu_power = get_avg(avg_gpu_power_list)
                    gpu_power_chart.title = "".join([
                        "GPU Power: ",
                        '{0:.2f}'.format(gpu_power_W),
                        "W - avg: ",
                        '{0:.2f}'.format(avg_gpu_power),
                        "W - peak: ",
                        '{0:.2f}'.format(gpu_peak_power),
                        "W"
                    ])
                    gpu_power_chart.append(gpu_power_percent)

                    ui.display()

            time.sleep(args.interval)

        except KeyboardInterrupt:
            break

    return powermetrics_process


if __name__ == "__main__":
    powermetrics_process = main()
    powermetrics_process.terminate()
    print("Successfully terminated powermetrics process")
