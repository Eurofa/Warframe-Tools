from bs4 import BeautifulSoup as bs
import requests
import re

base = "https://warframe.market/items"

def wrtie_to_file(content):
    f = open('output.txt', 'a')
    counter = 0
    for line in content:
        f.write(str(line))
        if counter%2 == 1:
            f.write('\n')
        else:
            f.write(' ')
        counter += 1
    f.close()

def setup(url):
    url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #.text is in unicode, .content is in bytes
    data = requests.get(url, headers = headers).text
    return data

def filter(content):
    pass


data = setup(url)
soup = bs(data, 'html.parser')

# Find relevant <div> tag with a specific class (find via inspect)
content = soup.find_all('div', {'class': 'card-body'})

# Separate source by \n's
filtered = filter(str(content).split('\n'))

wrtie_to_file(filtered)

print('Complete')