import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

# Inside the IO-bound function, we ask the CPU to sit idle and pass time 
# whereas, inside the CPU-bound function, the CPU is going to be busy churning out a few numbers. 
COUNT = 600000000
SLEEP = 10
 
def io_bound(sec):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished sleeping...")
 
def cpu_bound(n):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Start counting...")
 
    while n>0:
        n -= 1
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished counting...")
