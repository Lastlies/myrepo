
pol = input("Введите пол (м/ж): ")
vozv = int(input("Введите возраст: "))
if pol.lower() =="м":
    pens_vozv = 60
elif pol.lower() =="ж":
    pens_vozv = 60
else:
    print("некорректно указан пол")
    exit()

if vozv >= pens_vozv:
    print ("пора на пенсию")
else:
    print ("еще рано)")