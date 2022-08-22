import threading
import time

def thread_1():
    while True:
        print("thread1 work")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

while True:
    print("main work")
    time.sleep(2.0)
    
# 메인을 종료하면 쓰레드도 꺼짐
# thread1 work
# main work
# thread1 work
# main work
# thread1 work
# thread1 work
# main work
# thread1 work
# thread1 work
# main work
# thread1 work
# thread1 work
# main work
# thread1 work
# thread1 work