import requests

from bs4 import BeautifulSoup

act_index = int(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
act_list = soup.find_all('a')
print(act_list[act_index - 1])
