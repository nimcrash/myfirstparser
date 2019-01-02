import requests
from bs4 import BeautifulSoup
import argparse

param_parser = argparse.ArgumentParser()
param_parser.add_argument('count', help = 'количество выводимых книг', type = int, choices = range(0,101))
param_parser.add_argument('path', help = 'путь к файлу', type = argparse.FileType('w'))
args = param_parser.parse_args()

url = 'http://readrate.com/rus/ratings/top100'
r = requests.get(url)

soup = BeautifulSoup(r.text, features = 'html.parser')
books = soup.findAll('div', {'class':'info'})

for i in range(args.count):
    
    book = books[i].find('div', {'class' : 'title'}).find('a').text
    author = books[i].find('ul', {'class' : 'contributors-list list'}).find('a').text

    string = "%s - %s" % (book, author)
    
    print(string)
    args.path.write(string + '\n')

args.path.close()
