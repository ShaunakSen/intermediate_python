# url : http://alldistancebetween.com/in/by-alphabet/m/majestic+railway+station/?page=2
import csv
import requests
from bs4 import BeautifulSoup

# Now we have list of all links

# we can visit each link in this function and get info :)


# GLOABAL VARS WHICH WE WILL POPULATE AS WE GO ALONG

origins = []
destinations = []
distances = []

detailed_origins = []
detailed_destinations = []
detailed_distances = []
detailed_times = []


def csv_writer(data, data_headers):
    path = "myFile.csv"
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        # for line in data:
        #     writer.writerow(line)
        writer.writerow(data_headers)

        for line in data:
            try:
                writer.writerow(line)
            except:
                pass




def visit_links(all_links):
    web_visit_counter = 0
    for link in all_links   :

        print "Visiting link no: " + str(web_visit_counter+1)
        r1 = requests.get(link)
        soup1 = BeautifulSoup(r1.content, 'lxml')
        origins.append(soup1.find_all("span", {"id": "origin2"})[0].text)
        destinations.append(soup1.find_all("span", {"id": "destination2"})[0].text)
        distances.append(soup1.find_all("span", {"id": "distance2"})[0].text.strip())




        detailed_origins.append(soup1.find_all("td", {"id": "origin"})[0].text)
        # print detailed_origins
        detailed_destinations.append(soup1.find_all("td", {"id": "destination"})[0].text)
        # print detailed_destinations
        detailed_distances.append(soup1.find_all("td", {"id": "driving-distance"})[0].text)
        # print detailed_distances
        detailed_times.append(soup1.find_all("td", {"id": "driving-time"})[0].text)
        # print detailed_times

        # print origins
        # print destinations
        # print distances

        web_visit_counter += 1
        print "Done with link no: " + str(web_visit_counter)

    print "Done!!"
    print len(detailed_origins)
    print len(detailed_destinations)
    print len(detailed_distances)
    print len(detailed_times)


    for origin in detailed_origins:
        origin.encode("utf-8")
    for destination in detailed_destinations:
        destination.encode("utf-8")

    for distance in detailed_distances:
        distance.encode("utf-8")

    for time in detailed_times:
        time.encode("utf-8")

    data_headers = ["origin", "destination", "driving-distance", "driving-time"]
    data_to_write = [detailed_origins, detailed_destinations, detailed_distances, detailed_times]
    final_data = zip(*data_to_write)
    print final_data

    csv_writer(final_data, data_headers)


    print("Writing done!!")








url = 'http://alldistancebetween.com/in/by-alphabet/m/majestic+railway+station/?page=2'

root_url = 'http://alldistancebetween.com'

r = requests.get(url)
# r.content
soup = BeautifulSoup(r.content, 'lxml')

table_data = soup.find_all("td")

all_links = []
all_link_texts = []

for td in table_data:
    all_link_texts.append(td.contents[0].text)
    all_links.append(root_url + td.contents[0].get("href"))



# print all_link_texts
# print all_links


# for link in all_links:
#     print link


visit_links(all_links)
