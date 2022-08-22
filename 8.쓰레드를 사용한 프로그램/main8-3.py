import threading

def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")
        
t1 = threading.Thread(target=sum, args=('thread1>> ', 10))
t2 = threading.Thread(target=sum, args=('thread2>>>>>>>>', 10))

t1.start()
t2.start()

print("main thread")

# thread1>>  : 0
# thread1>>  : 1
# thread1>>  : 2
# main thread
# thread2>>>>>>>> : 0
# thread1>>  : 3
# thread1>>  : 4
# thread1>>  : 5
# thread1>>  : 6
# thread1>>  : 7
# thread2>>>>>>>> : 1
# thread2>>>>>>>> : 2
# thread2>>>>>>>> : 3
# thread2>>>>>>>> : 4
# thread2>>>>>>>> : 5
# thread2>>>>>>>> : 6
# thread1>>  : 8
# thread2>>>>>>>> : 7
# thread1>>  : 9
# thread2>>>>>>>> : 8
# thread2>>>>>>>> : 9