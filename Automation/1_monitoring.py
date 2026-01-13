# doing moingtoring monitoring

import psutil
import time

def monitor_system():
    print("Monitoring system...")   
    # Add monitoring logic here
    # For example, checking CPU usage, memory usage, etc.
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    # print(f"CPU Usage: {cpu_usage}%")
    # print(f"Memory Usage: {memory_usage}%")         

    return f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%"


print(monitor_system())