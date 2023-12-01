user_data = input("Введите число:")
N = int(user_data)
before_last = last = current = 1
for i in range(N):
    current = last + before_last
    before_last = last
    last = before_last + last
    print(current)