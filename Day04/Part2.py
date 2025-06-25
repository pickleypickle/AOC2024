import csv

def read_input(filename):
    text_list = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            text_list.extend(row)
    return text_list

def count_XMAS(text1, text2):
    if (text1 == "MAS" or text1 == "SAM") and (text2 == "MAS" or text2 == "SAM"):
        return 1
    
    return 0

def word_search(data):
    count = 0

    # Loop through text to find "A"
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'A':
                # Check if any diagonal direction is out of bounds
                if i + 1 < len(data) and i - 1 >= 0 and j + 1 < len(data[0]) and j - 1 >= 0:
                    # Check matchups for MAS
                    first_diagonal = data[i - 1][j - 1] + 'A' + data[i + 1][j + 1]
                    second_diagonal = data[i - 1][j + 1] + 'A' + data[i + 1][j - 1]

                    count += count_XMAS(first_diagonal, second_diagonal)

    return count

def main():
    data = read_input('Day04/input.csv')
    XMAS_count = word_search(data)
    print("Number of 'X-MAS' occurrences:", XMAS_count)

if __name__ == '__main__':
    main()