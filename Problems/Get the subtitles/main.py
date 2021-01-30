import requests
from bs4 import BeautifulSoup


index = int(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
art = soup.find_all('h2')
print(art[index].text)
