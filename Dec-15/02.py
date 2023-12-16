

try:
    fd = open("input.txt", 'r', encoding='utf8')
except FileNotFoundError:
    print('файл не найден')
    exit()
else:
    text = fd.read()
    fd.close()
    print(text)
    first_word = input("Ввеите исходное слово: ")
    need_to_change = input("Введите исходное слово: ")
    mod_text = text.replace(first_word.lower(), need_to_change.lower())
    mod_text = mod_text.replace(first_word.upper(), need_to_change.upper())
    mod_text = mod_text.replace(first_word.capitalize(), need_to_change.capitalize())



    fd2 = open("output.txt", "w", encoding="utf8")
    fd2.write(mod_text)

         


    fd2.close()