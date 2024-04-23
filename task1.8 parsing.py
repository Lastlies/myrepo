#8.	Написать программу, которая  предоставляет пользователю возможность ввести с клавиатуры
# количество рублей, и переводит его в доллары и евро

import requests
from bs4 import BeautifulSoup

url = "https://finance.rambler.ru/currencies/"

source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')


divs = soup.find_all("div", class_="currency-table__base")


