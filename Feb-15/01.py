import threading
data = [1, 2, 3, 4, 5]
result = []
threads = []

def process_item(item):
    result.append(item * 2)

for item in data:
    thread = threading.Thread(target=process_item, args=(item))
    threads.append(result)
    thread.start()

for threaf in threads:
    thread.join()

print(result)

# параллельность языков
# гил gil
# процессинг
# мульти процессинг