import requests
from bs4 import BeautifulSoup
url = "https://www.example.com"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
h1_element = soup.find('h1')
if h1_element:
    print("Заголовок (тег <h1>):")
    print("Текст: ", h1_element.text)
    print("Атрибути: ", h1_element.attrs)
else:
    print("Заголовок (тег <h1>) не знайдено на сторінці.")
