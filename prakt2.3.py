#Ввести натуральное число и определить, верно ли,
# что в его записи есть две одинаковые цифры, стоящие рядом.

a = input("Введите натуральное число: ")

for i in range(1, len(a)):
    while a[i] == a[i - 1]:
        print("В числе есть две одинаковые цифры, стоящие рядом.")
        break
else:
    print("В числе нет двух одинаковых цифр, стоящих рядом.")

    #ошибка вывода в случае если есть 2 одинаковых числа. запутался в циклах в циклах