import requests as re
from bs4 import BeautifulSoup as bs


def scrape():
    with open('tanggal.txt', 'r') as file:
        count = 0
        for line in file:
            count += 1
            halaman = re.get(f'https://onejav.com/{line.strip()}')
            nama_file = line.strip().replace('/', '-')
            pencarian = bs(halaman.content, "html.parser")
            with open(f'torrent{nama_file}.txt', 'w+') as generated:
                for judul in pencarian.findAll('a', 'button is-primary is-fullwidth'):
                    generated.writelines(f'https://onejav.com{judul['href']}\n')
                    print(f'{nama_file}.txt berhasil dibuat....')
                generated.close()

scrape()