# url : https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA

# div class = "info"

# This class contains our data


import requests
from bs4 import BeautifulSoup

url = 'https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'

r = requests.get(url)
# r.content
soup = BeautifulSoup(r.content, 'lxml')

# print(soup.prettify())


# Returns a list of all links
# print(soup.find_all('a'))

# for link in soup.find_all('a'):
#     print(link.get('href'))
#
#
# for link in soup.find_all('a'):
#     print(link.text)


for link in soup.find_all('a'):
    if "http" in link:
        print("<a href = '%s'>%s</a>" %(link.get("href"), link.text))


general_data = soup.find_all("div", {"class": "info"})

# for item in general_data:
#     print(item.text)

# NOTE: item.contents is v imp

for item in general_data:
    # print(item.text)
    # print(item.contents)
    # print(item.contents[0].text)
    # print(item.contents[1].text)
    print(item.contents[0].find_all("a", {"class": "business-name"}))[0].text
    print(item.contents[1].find_all("p", {"class": "adr"})[0].text)

    print(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
    print(item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text)
    print(item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text)
    print(item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)

    try:
        print(item.contents[1].find_all("div", {"class": "primary"})[0].text)
    except:
        pass
