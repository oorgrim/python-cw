# ассинхронность
# мгогопоточность

import threading
import time

def worker_function():
    print('Работник выполняет задачу')
    n = 0
    for i in range(100):
        n += i % 3
    time.sleep(10)
    print('закончил работать', n)
    
# создание потока
thread = threading.Thread(target=worker_function)

# запуск потока
thread.start()
print("основной поток") 

# thread.join()
exit()