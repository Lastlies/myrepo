#A»: Заполнить массив случайными числами в интервале [-10,10]
# и отобрать в другой массив все чётные отрицательные числа.
import random
array = [random.randint(-10, 10) for _ in range(10)] #randint(): возвращает случайное число из определенного диапазона
result = [num for num in array if num < 0 and num % 2 == 0]
print("Исходный массив случайных чисел:", array)
print("Массив четных отрицательных чисел:", result)