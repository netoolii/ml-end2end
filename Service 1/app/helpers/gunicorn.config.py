import multiprocessing

bind = ":8080"
cpu_count = multiprocessing.cpu_count()
workers = cpu_count * 2 + 1
threads = 2 * cpu_count
proc_name = "service_01_api"
timeout = 6000
