import bs4 as bs

import urllib.request

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# print(soup)

# Get title

print(soup.title)

print(soup.title.string)

# First paragraph

print(soup.p)


# print(soup.find_all('p'))


# .string doesnt work if u have child tags

for paragraph in soup.find_all('p'):
    print(paragraph.text)


# Get all the text

# print(soup.get_text())

# Find all links


for url in soup.find_all('a'):
    print(url.text)
    print(url.get('href'))



# Get the nav

nav = soup.nav

# print(nav)

for url in nav.find_all('a'):
    print(url.get('href'))


body = soup.body

# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# find div with class

for div in soup.find_all('div', class_ = 'body'):
    print(div.text)




# scrape tables

table = soup.table

# print(table)

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

    
