import re
a = input("Введите номер автомобиля РФ формата У666СM78: ")
b = re.compile(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}')
if re.fullmatch(b,a):
    print("номер указан верно")
else:
    print("номер указан неверно")