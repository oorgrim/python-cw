user_data1 = input(" Введите первое число: ")
user_data2 = input(" Введите второе число: ")
sign = input(" Введите знак: ")
try:
    num1, num2 = int(user_data1), int(user_data2)
except ValueError:
    print("Должно быть число, введите число!")
else:
    match sign:  
        case "+":
            print("Сумма ваших чисел равна ", num1 + num2)
            
        case "-":
            print("РАзность ваших чисел равна", num1 - num2)
            print("РАзность ваших чисел равна", num2 - num1)
            
        case "*":
            print("Произведение ваших чисел равно ", num1 * num2)
            
        case "/":
            print("Деление ваших чисел равно", num1 / num2)
            print("Деление ваших чисел равно", num2 / num1)
        case _:
            print("Введите *, /, + или -")