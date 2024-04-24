#Ввести натуральное число и определить, верно ли,
# что в его записи есть две одинаковые цифры, стоящие рядом.


while True:
    value = input("Введите натуральное число или введите x для выхода: ")
    if value == "x":
        break
    elif (value.isdigit()) and (int(value) % 1 == 0):
        for i in range(len(list(value))):
            if i == len(value) - 1:
                print("В числе нет двух одинаковых цифр, стоящих рядом.")
                break
            elif value[i] == value [i + 1]:
                print("В числе есть две одинаковые цифры, стоящие рядом.")
                break
    else:
        print("Неправильный ввод!")
