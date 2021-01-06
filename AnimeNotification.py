import datetime #pegar data atual
import time
import requests #pegar os dados da página de internet
import pandas as pd #guardar dados
from bs4 import BeautifulSoup #pegar dados de HTML e XML
from plyer import notification #notificação no pc

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

lancamento = None
try:
    page

except:
    print("Por favor! Verifique a conexão de internet")

if (lancamento != None):
    data = lancamento.json(['Sucesso'])

    while(True):
        notification.notify(
            title = 'Lançamento',
            message = '{nome}\n{data}',
            app_icon = 'Paomedia-Small-N-Flat-Bell.ico',
            timeout = 60
        )
        time.sleep(60*60*1)