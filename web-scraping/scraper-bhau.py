import csv
import requests
from bs4 import BeautifulSoup


url = 'http://www.anubandh.com/marriage_bureau/profile_table.jsp?user_id=18175'

labels = []
values = []

r = requests.get(url)
# r.content
soup = BeautifulSoup(r.content, 'lxml')

tables = soup.find_all("table")

required_table = tables[0]

table_rows = required_table.find_all("tr")
first_table_row = table_rows[0]

first_table_data = first_table_row.find_next_siblings("tr")[0]

first_table_data_left = first_table_data.find_all("td")[0]
# print first_table_data_left

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

print big_table_tr_2
