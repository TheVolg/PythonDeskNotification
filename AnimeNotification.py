import datetime #pegar data atual
import time #pegar o tempo transcorrido?
import requests #pegar os dados da página de internet
from bs4 import BeautifulSoup #pegar dados de HTML e XML
from plyer import notification #notificação no pc

page = None
URL = 'https://animesonehd.xyz'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

animes = soup.find_all(class_='sContainer')

for anime in animes:
    nome = anime.find('div', class_='EpisodiosDesc').text.strip()
    data = anime.find('div', class_='EpisodiosData').text.strip()
    print(nome)
    print(data)
    print()

"""  
try:
   page

except:
    print("Por favor! Verifique a conexão de internet")

if (page != None):

    while(True):
        notification.notify(
            title = 'Lançamento',
            message = anime,
            app_icon = 'E:/GitKraekn Local Repo/PythonDeskNotification/J.ico',
            timeout = 60
        )
        time.sleep(60*60*1)
"""