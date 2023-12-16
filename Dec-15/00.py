try:
    fd = open("./input.txt", encoding='utf8')    #файловый дескриптор
except FileNotFoundError:
    print('файл не найден')
    exit()

text = fd.read() #прочитать 2048 байтов,  если не указывать цифру, то прочтется все
fd.close()

new_text = text.upper()
print(text)


fd2 = open("output.txt", "w", encoding="utf8")
fd2.write(new_text)
fd2.close()
# если путь указан полностью, каталоги разделять \\