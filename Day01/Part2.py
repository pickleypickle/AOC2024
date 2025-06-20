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

# Calculate similarity scores for each number in list 1 (num*appearances in list 2)
def calculate_similarity(list1, list2):
    similarity_list = []

    for num in list1:
        appearances = list2.count(num)
        similarity_list.append(int(num) * appearances)

    return similarity_list

def main():
    filename = 'Day01/numbers.csv'
    list1, list2 = read_csv(filename)
    
    # Calculate the similarity scores
    similarity_scores = calculate_similarity(list1, list2)

    # Printing results
    print("Sum of similarity scores:", sum(similarity_scores))

if __name__ == '__main__':
    main()

# This code reads a CSV file containing two lists of numbers, calculates the similarity scores based on the number of appearances in the second list, and prints the sum of these scores.