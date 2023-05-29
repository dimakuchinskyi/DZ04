import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
h2_tags = soup.find_all('h2')

for h2 in h2_tags:
    print(h2.text)
