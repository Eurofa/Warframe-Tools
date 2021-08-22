from bs4 import BeautifulSoup as bs
import requests
import re

original = "https://www.carsales.com.au/cars/audi/a5/"

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
    # Filter our result
    filtered = []
    revised = []
    for line in content:
        if not ('sv-title' not in line and 'sv-price' not in line):
            filtered.append(line)
    for line in filtered:
        line_list = line.split('>')
        for section in line_list:
            if 'Audi A5' in section or '$' in section:
                clean = section.split('<')[0]
                clean = clean.strip(' ')
                clean = clean.strip('*')
                clean = clean.strip('$')
                if len(clean) > 10:
                    clean = clean.split(' ')[0]
                revised.append(clean)
    return revised


data = setup(original)
soup = bs(data, 'html.parser')

# Find relevant <div> tag with a specific class (find via inspect)
content = soup.find_all('div', {'class': 'card-body'})

# Separate source by \n's
filtered = filter(str(content).split('\n'))

wrtie_to_file(filtered)

print('Complete')