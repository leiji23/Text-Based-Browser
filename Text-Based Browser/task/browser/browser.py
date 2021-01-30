import argparse
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore


parser = argparse.ArgumentParser()
parser.add_argument("dir")  # dir=saved_files
args = parser.parse_args()  # read the argument: 'saved_files'
my_history = deque()

if not os.access(args.dir, os.F_OK):
    os.mkdir(args.dir)  # create directory: 'saved_files'

current_page = ''
while True:
    file_list = os.listdir(args.dir)
    url = input()
    if url == 'exit':  # may not be needed
        break
    else:
        try:
            r = requests.get('https://' + url)
        except requests.exceptions.ConnectionError:
            print('Error: Incorrect URL')
            break
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            all_tags = soup.find_all()
            content = ''

            for tag in all_tags:
                if tag.name == 'a':
                    print(Fore.BLUE, tag.text)
                content += tag.text
                print(tag.text)
            file_path = os.path.join(args.dir, url)
            file_write = open(file_path, 'w', encoding='utf-8')
            current_page = url
            my_history.append(url)
            file_write.write(content)
            file_write.close()

