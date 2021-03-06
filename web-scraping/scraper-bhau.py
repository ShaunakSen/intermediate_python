import csv
import requests
from bs4 import BeautifulSoup







url = 'http://www.anubandh.com/marriage_bureau/profile_table.jsp?user_id=20000'

scrape_counter = 0


#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    global user_ids
    reader = csv.reader(file_obj)
    for row in reader:
        for user_id in row:
            if user_id not in user_ids:
                user_ids.append(user_id)
    print user_ids
#----------------------------------------------------------------------

#----------------------------------------------------------------------
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
#----------------------------------------------------------------------



def scrape_url(url, user_id):

    global scrape_counter
    print "scraping link no:", scrape_counter+1, "for id: ", user_id

    labels_all = []
    values_all = []

    labels = []
    values = []


    labels2 = []
    values2 = []

    labels3 = []
    values3 = []

    labels4 = []
    values4 = []


    r = requests.get(url)
    # r.content
    soup = BeautifulSoup(r.content, 'lxml')

    tables = soup.find_all("table")

    required_table = tables[0]

    table_rows = required_table.find_all("tr", class_ = True)
    #print table_rows[0]
    first_table_row = table_rows[0]
    #print first_table_row

    first_table_data = first_table_row.find_next_siblings("tr")[0]
    #print first_table_data

    first_table_data_left = first_table_data.find_all("td")[0]
    # print first_table_data_left

    if len(first_table_data_left.find_all("tr")) == 0:
        print "skipping for user id:", user_id
        return
    first_table_data_left_trs = first_table_data_left.find_all("tr")[0]
    siblings = first_table_data_left_trs.find_next_siblings("tr")

    general_info = siblings[len(siblings)-1]
    # print general_info

    general_info_labels = general_info.find_all("b")

    del general_info_labels[1]

    for label in general_info_labels:
        labels.append(label.string)

    general_info_values = general_info.find_all("span")

    for value in general_info_values:
        values.append(value.string)

    # print values

    big_table_data = first_table_row.find_next_siblings("tr")[1].find_all("table", limit = 1)[0]

    big_table_tr_1 = big_table_data.find_all("tr", limit=1)[0]
    # print big_table_trs

    big_table_tr_1_siblings = big_table_tr_1.find_next_siblings("tr")

    big_table_tr_2 = big_table_tr_1_siblings[0]
    big_table_tr_3 = big_table_tr_1_siblings[1]

    # scraping big_table_tr_1

    big_table_tr_1_labels = big_table_tr_1.find_all("b")

    for label in big_table_tr_1_labels:
        labels2.append(label.string)


    big_table_tr_1_values = big_table_tr_1.find_all("span", {"class": "login"})

    for value in big_table_tr_1_values:
        values2.append(value.string)

    # print values2



    big_table_tr_2_labels = big_table_tr_2.find_all("b")

    for label in big_table_tr_2_labels:
        labels3.append(label.string)


    big_table_tr_2_values = big_table_tr_2.find_all("span", {"class": "login"})

    for value in big_table_tr_2_values:
        values3.append(value.string)


    big_table_tr_3_labels = big_table_tr_3.find_all("b")

    for label in big_table_tr_3_labels:
        labels4.append(label.string)


    big_table_tr_3_values = big_table_tr_3.find_all("span", {"class": "login"})

    for value in big_table_tr_3_values:
        values4.append(value.string)

    # sanitary check


    if len(labels) == len(values) and len(labels2) == len(values2) and len(labels3) == len(values3) and len(labels4) == len(values4):
        print "Good to go!"
        for label in labels:
            labels_all.append(label)
        for label in labels2:
            labels_all.append(label)
        for label in labels3:
            labels_all.append(label)
        for label in labels4:
            labels_all.append(label)
        for value in values:
            values_all.append(value)
        for value in values2:
            values_all.append(value)
        for value in values3:
            values_all.append(value)
        for value in values4:
            values_all.append(value)

    i = 0
    for value in values_all:
        if value is not None:
            value = value.encode("utf-8")
            values_all[i] = " ".join(value.split())
            values_all[i] = values_all[i].replace(',', ' ')
        else:
            values_all[i] = "Not specified"
        i += 1
    print values_all
    values_all.insert(0, user_id)

    i = 0
    for label in labels_all:
        if label is not None:
            label = label.encode("utf-8")
            labels_all[i] = " ".join(label.split())
            labels_all[i] = labels_all[i].replace(',', ' ')
        else:
            labels_all[i] = "Not specified"

        i += 1
    print labels_all

    labels_all.insert(0, "id")




    print "Done............."
    scrape_counter += 1
    if scrape_counter == 1:
        csv_writer([labels_all, values_all], "out.csv")
    else:
        csv_writer([values_all], "out.csv")


user_ids = []

root_url = 'http://www.anubandh.com/marriage_bureau/profile_table.jsp?user_id='

urls_to_scrape = []

min_url = int(raw_input("Enter min id: "))
max_url = int(raw_input("Enter max id: "))

for i in range(min_url, max_url+1):
    user_ids.append(i)

csv_path = "input.csv"
#with open(csv_path, "rb") as f_obj:
    #csv_reader(f_obj)

for user_id in user_ids:
    urls_to_scrape.append(root_url + str(user_id))



for x in range(len(urls_to_scrape)):
    scrape_url(urls_to_scrape[x], user_ids[x])
