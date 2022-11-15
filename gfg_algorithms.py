import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.geeksforgeeks.org/fundamentals-of-algorithms/?ref=shm')
soup = BeautifulSoup(r.content, 'html.parser')

# title tag- Python
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)

# content
s = soup.find('div', class_='entry-content')
lines = s.find_all('p')
for line in lines:
    print(line.text)

# leftbar
s = soup.find('div', id= 'main')
leftbar = s.find('ul', class_='leftBarList')
lines = leftbar.find_all('li')
for line in lines:
    print(line.text)

#links
for link in soup.find_all('a'):
    print(link.get('href'))

#images
images_list = []
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
for image in images_list:
    print(image)
