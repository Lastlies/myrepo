# программа позволяет вывести ip адрес, имя хоста, и расчитать диапозон ip адресации по маске и адресу
from calculate1 import *
from help import help1
from my_ip import myip
import pyfiglet

print(pyfiglet.figlet_format("GET IP"))

while True:
    print("Если необходимо вызвать справку введите -help \nДля выхода из программы введите X")
    a = str(input())
    if a.lower() == "x":
        break
    elif a == "-help":
         help1()
    elif a == "-myip":
         myip()
    elif a == "-ipcalculate":

            ip_address = input("Введите IP адрес: ")
            subnet_mask = input("Введите двухзначную маску подсети (от 0 до 32): ")

            if validate_ip(ip_address) and validate_subnet(subnet_mask):
                print("Корректный IP адрес и маска подсети")

                network_address = calculate_network_address(ip_address, subnet_mask)
                broadcast_address = calculate_broadcast_address(network_address, subnet_mask)
                first_host = calculate_first_host(network_address)
                last_host = calculate_last_host(broadcast_address)

                print("IP адрес:", ip_address)
                print("Маска сети:", subnet_mask)
                print("Адрес сети:", network_address)
                print("Широковещательный адрес:", broadcast_address)
                print("IP адрес 1-го узла:", first_host)
                print("IP адрес последнего узла:", last_host)
            else:
                print("Некорректный IP адрес или маска подсети")



