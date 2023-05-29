import requests
from bs4 import BeautifulSoup
url = "https://www.example.com"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
example_elements = soup.find_all(class_="example-class")
for element in example_elements:
    print(element)
