
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

def calculate_difference(list1, list2):
    # Sorting lists in ascending order
    list1.sort()
    list2.sort()

    # Calculating differences
    return [abs(int(a) - int(b)) for a, b in zip(list1, list2)]

def main():
    filename = 'Day01/numbers.csv'
    list1, list2 = read_csv(filename)
    
    # Calculate the difference
    list_diff = calculate_difference(list1, list2)

    # Printing results
    print("Sum of differences:", sum(list_diff))

if __name__ == '__main__':
    main()