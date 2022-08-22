import threading
import time

def thread_1():
    while True:
        print("쓰레드1")
        time.sleep(1.0)
t1 = threading.Thread(target=thread_1)
t1.start()

while True:
    print("main work")
    time.sleep(2.0)
    
# 쓰레드1
# main work
# 쓰레드1
# main work
# 쓰레드1
# 쓰레드1
# main work
# 쓰레드1
# 쓰레드1
# main work
# 쓰레드1
# 쓰레드1
# main work
# 쓰레드1
# 쓰레드1
# main work
# 쓰레드1

# KeyboardInterrupt
# 쓰레드1
# 쓰레드1
# 쓰레드1
# 쓰레드1
# 쓰레드1
# 쓰레드1
# 쓰레드1
