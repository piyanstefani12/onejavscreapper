import requests as re
from bs4 import BeautifulSoup as bs


def scrape(page):
    url = page
    halaman = re.get(url)
    pencarian = bs(halaman.content, "html.parser")
    for judul in pencarian.findAll('a', 'magnet-click-track'):
        print(judul['href'])

scrape(page=input("Masukkan Pencarian:"))