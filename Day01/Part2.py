import csv

def read_csv(filename):
    list1 = []
    list2 = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Split by spaces
            row = [elem.strip().split('   ') for elem in row]
            list1.append(row[0][0])
            list2.append(row[0][1])
    return list1, list2