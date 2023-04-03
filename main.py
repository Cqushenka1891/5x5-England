
import urllib.request


from bs4 import BeautifulSoup
import requests
response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
#перевірка підключення
if response.status_code == 200:
#об'єкт парсінгу - назва сторінки та обробника
   soup = BeautifulSoup(response.text, features="html.parser")
   soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})
   dollar = float(soup_list[7].text.replace(",", "."))
   print(dollar)
   grivna = float(input("Введите кол-во грн: "))
   print(grivna/dollar)
