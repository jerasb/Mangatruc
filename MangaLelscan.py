import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
from PIL import Image

if __name__ == '__main__':
    def dossier():
                os.chdir("C:\\Users\\jeras\\Desktop\\test")
    dossier()


path = r"C:\Users\jeras\Desktop\test"
CompteurParcours = 0

url = "https://www.lelscan-vf.com/manga/shingeki-no-kyojin/126"



def RecupListeLiens(soup):
    Div = soup.findAll('div')
    L = []
    Img = soup.findAll('img')
    for item in Img:
        if 'data-src' in item.attrs:
            L.append(item['data-src'])
    return L


def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]




def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    LL = []
    for a in A:
        if 'class' in a.attrs and a['class'] == ['btn','next_page']:
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl


def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['page-break'])
    return bool









