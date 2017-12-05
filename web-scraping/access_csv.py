import csv
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]

#----------------------------------------------------------------------
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        # for line in data:
        #     writer.writerow(line)
        for item in data[0]:
            new_list = []
            new_list.append(item)
            new_list.append(list1[item - 1])
            new_list.append(list2[item - 1])
            writer.writerow(new_list)


#----------------------------------------------------------------------
if __name__ == "__main__":
    data = [[1,2,3,4],list1, list2]
    path = "myFile.csv"
    csv_writer(data, path)
