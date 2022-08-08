import requests
import bs4
gorod = input("Input weather in: ")

def get_weather(url):
        response = requests.get(url)
        bs = bs4.BeautifulSoup(response.text,"html.parser")
        temp = bs.find('div', class_ = 'temp fact__temp fact__temp_size_s')
        print(temp.text)

match gorod:
    case "Minsk": get_weather(url = 'https://yandex.com.am/weather/?lat=53.90228653&lon=27.56183243')
    case "Gomel": get_weather(url = 'https://yandex.com.am/weather/?lat=52.42416382&lon=31.01428032')
    case "Grodno": get_weather(url = 'https://yandex.com.am/weather/?lat=53.67783737&lon=23.82953072')
    case _: print('Нет такого города!')



