import requests, csv
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

url = 'https://www.imdb.com/chart/top/'
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

titulos = [titulo.text for titulo in soup.find_all('h3', class_="ipc-title__text")][1:-1]

# print(f"{'TÍTULOS'.center(30, '-')}")

# for titulo in titulos:
#     print(f'- {titulo}')

with open ('filmes.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Título'])  
    escritor.writerows([[titulo] for titulo in titulos])

with open ('filmes.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
