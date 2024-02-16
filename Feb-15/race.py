import threading
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_lock = threading.Lock()

def my_func():
    global numbers
    for _ in range(100000):
        my_lock.acquire()
        
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                numbers[i] += numbers[i] - numbers[i-1] + 1

            else:

                numbers[i] += numbers[i + 1] - numbers[i]
        my_lock.release()



thr1 = threading.Thread(target=my_func)
thr2 = threading.Thread(target=my_func)
thr1.start()
thr2.start()

thr1.join()
thr2.join()

print(numbers)