import requests
from bs4 import BeautifulSoup
url = 'https://www.example.com'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
for table in tables:
    print(table)
    print('\n')
