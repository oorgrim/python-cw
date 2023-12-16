

try:
    fd = open("mystat_input.txt", 'r', encoding='utf8')
except FileNotFoundError:
    print('файл не найден')
    exit()
else:
    text = fd.read()
    fd.close()
    print(text)
    protocol = text.find('://')
    if protocol != -1:
        a = text[:protocol]
        text = text[protocol + 3:]
    else:
        a = ''

    domain = text.find('/')
    if domain != -1:
        a = text[:domain]
        text = text[domain:]
    else:
        a = domain = ''



    fd2 = open("mystat_output.txt", "w", encoding="utf8")
    # fd2.write(mod_text)

    fd2.close() 