#Функция для проверки корректности IP-адреса
def validate_ip(ip_address):


    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True


#Функция для проверки корректности маски подсети
def validate_subnet(subnet_mask):


    if len(subnet_mask) != 2:
        return False
    if not subnet_mask.isdigit() or not 0 <= int(subnet_mask) <= 32:
        return False
    return True


 #Функция для вычисления сетевого адреса
def calculate_network_address(ip_address, subnet_mask):


    ip_parts = [int(part) for part in ip_address.split('.')]
    mask_length = int(subnet_mask)

    # Вычисляем бинарное представление маски подсети
    binary_mask = '1' * mask_length + '0' * (32 - mask_length)

    # Разбиваем бинарное представление маски подсети на октеты
    mask_parts = [binary_mask[i:i + 8] for i in range(0, 32, 8)]

    # Преобразуем бинарные октеты в десятичные числа
    mask_decimals = [int(part, 2) for part in mask_parts]

    # Применяем маску подсети к IP-адресу
    network_address = [str(ip_parts[i] & mask_decimals[i]) for i in range(4)]
    return '.'.join(network_address)


#Функция для вычисления широковещательного адреса
def calculate_broadcast_address(network_address, subnet_mask):


    ip_parts = [int(part) for part in network_address.split('.')]
    mask_length = int(subnet_mask)

    # Вычисляем бинарное представление инвертированной маски подсети
    inverted_binary_mask = '0' * mask_length + '1' * (32 - mask_length)

    # Разбиваем бинарное представление инвертированной маски подсети на октеты
    inverted_mask_parts = [inverted_binary_mask[i:i + 8] for i in range(0, 32, 8)]

    # Преобразуем бинарные октеты в десятичные числа
    inverted_mask_decimals = [int(part, 2) for part in inverted_mask_parts]

    # Применяем инвертированную маску подсети к IP-адресу
    broadcast_address = [str(ip_parts[i] | inverted_mask_decimals[i]) for i in range(4)]
    return '.'.join(broadcast_address)


# Функция для вычисления IP-адреса первого узла
def calculate_first_host(ip_address):

    ip_parts = [int(part) for part in ip_address.split('.')]
    ip_parts[3] += 1
    return '.'.join(map(str, ip_parts))



#Функция для вычисления IP-адреса последнего узла
def calculate_last_host(broadcast_address):

    ip_parts = [int(part) for part in broadcast_address.split('.')]
    ip_parts[3] -= 1
    return '.'.join(map(str, ip_parts))
