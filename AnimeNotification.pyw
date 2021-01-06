import datetime #pegar data atual
import time #pegar o tempo transcorrido?
import requests #pegar os dados da página de internet
import json #ler/gravar json
from bs4 import BeautifulSoup #pegar dados de HTML e XML
from plyer import notification #notificação no pc

URL = 'https://animesonehd.xyz'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

animes = soup.find_all(class_='sContainer')

for anime in animes:
    nome = anime.find('div', class_='EpisodiosDesc').text.strip()
    data = anime.find('div', class_='EpisodiosData').text.strip()
novo = nome + '\n' + data

with open('comparativo.txt') as json_file:
    comparacao = json.load(json_file)

if (nome != comparacao):

    while(True):

        notification.notify(
            title = 'Lançamento',
            message = novo,
            app_icon = 'E:/GitKraekn Local Repo/PythonDeskNotification/J.ico',
            timeout = 10
        )
        with open('comparativo.txt', 'w') as outfile:
            json.dump(nome, outfile, ensure_ascii=False)
        time.sleep(60*1)

else:
     time.sleep(60*1)