try:
    fd = open("input.txt", encoding='utf8')    #файловый дескриптор
except FileNotFoundError:
    print('файл не найден')
    exit()

text = fd.read() #прочитать 2048 байтов,  если не указывать цифру, то прочтется все
fd.close()

new_text = text.upper()
print(text)

try:
    fd2 = open("C:\\Windows\\System\\output.txt", "w", encoding="utf8")
except PermissionError:
    print("В этом каталоге нельзя создавать файлы!")
    exit()

fd2.write(new_text)
fd2.close()
# если путь указан полностью, каталоги разделять \\