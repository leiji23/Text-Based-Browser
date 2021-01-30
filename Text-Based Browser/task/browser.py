import argparse
import os
from collections import deque
import requests


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


two_pages = ['bloomberg.com', 'nytimes.com']
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
    if url == 'exit':
        break
    elif url not in two_pages and url not in file_list and url != 'back':
        print('Error: Incorrect URL')
    elif url in two_pages:
        file_path = os.path.join(args.dir, url.strip('.com'))
        file_write = open(file_path, 'w', encoding='utf-8')
        if url == 'bloomberg.com':
            print(bloomberg_com)
            current_page = 'bloomberg.com'
            my_history.append('bloomberg')
            # if not os.access(file_path, os.F_OK):
            file_write.write(bloomberg_com)
            file_write.close()
        else:
            print(nytimes_com)
            current_page = 'nytimes.com'
            my_history.append('nytimes')
            file_write.write(nytimes_com)
            file_write.close()
    elif url == 'back':
        if len(my_history) != 0:
            back_page = my_history.pop()
            if back_page not in current_page:
                with open(os.path.join(args.dir, back_page), 'r', encoding='utf-8') as read_history:
                    print(read_history.read())
            else:
                with open(os.path.join(args.dir, my_history.pop()), 'r', encoding='utf-8') as read_history:
                    print(read_history.read())
    else:
        file_read = open(os.path.join(args.dir, url), 'r', encoding='utf-8')
        print(file_read.read())
        file_read.close()

        if url[0:7] != 'https://':
        url = 'https://' + url
    r = requests.get(url)
    print(r.text)
