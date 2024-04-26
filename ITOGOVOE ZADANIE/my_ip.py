import socket
import os

def myip():

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("\nИмя компьютера:" , socket.gethostname())
    print(f"IP адрес : {ip_address} \n")
