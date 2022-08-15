import psutil

# cpu = psutil.cpu_freq()
# print(cpu)

cpu_core = psutil.cpu_count(logical=False)
print(f"코어: {cpu_core} 개")

memory = psutil.virtual_memory()
memory_total = round(memory.total/1024**3) #total=17179869184
print(f"메모리: {memory_total}GB")

disk = psutil.disk_partitions()
print(disk)

for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total/1024**3)
    print(f'디스크 크기: {disk_total}')
    
net = psutil.net_io_counters
print(net)

# sent = round(net.bytes_sent/1024**2,1)
# recv = round(net.recv/1024**2,1)
# print(f'보내기 {sent}MB   받기:{recv}MB')