import csv

def read_input(filename):
    text_list = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            text_list.extend(row)
    return text_list
    
def word_search(data):
    # Loop through each row and count occurences of "XMAS" frontwards and backwards
    count = 0
    for line in data:
        count += line.count("XMAS") + line.count("SAMX")
    
    # Add vertical occurences through columns
    for col in range(len(data[0])):
        column_text = ''.join(line[col] for line in data)
        count += column_text.count("XMAS") + column_text.count("SAMX")

    # Add diagonal occurences top left to bottom right
    # Start from the bottom left corner and move diagonally up-right
    row = len(data)-1
    col = 0
    finished = False
    while not finished:
        if col == len(data[0])-1 and row == 0:
            finished = True
        else:
            # Join everything diagonal down-right from the current position

            diagonal_line =''
            for i in range (len(data)-1):
                # Check if we can go down-right
                if row+i < len(data) and col+i < len(data[0]):
                    # Add next character in the diagonal
                    diagonal_line += data[row+i][col+i]

            count += diagonal_line.count("XMAS") + diagonal_line.count("SAMX")

            # Move upwards until the top row, then right until the last column
            if row > 0:
                row -= 1
            else:
                col += 1

    # Add diagonal occurences top right to bottom left
    # Start from the bottom right corner and move diagonally up-left
    row = len(data)-1
    col = len(data[0])-1
    finished = False
    while not finished:
        if col == 0 and row == 0:
            finished = True
        else:
            # Join everything diagonal down-left from the current position

            diagonal_line =''
            for i in range (len(data)-1):
                # Check if we can go down-left
                if row+i < len(data) and col-i >= 0:
                    # Add next character in the diagonal
                    diagonal_line += data[row+i][col-i]

            count += diagonal_line.count("XMAS") + diagonal_line.count("SAMX")

            # Move upwards until the top row, then right until the last column
            if row > 0:
                row -= 1
            else:
                col -= 1


    return count
    
def main():
    data = read_input('Day04/input.csv')
    XMAS_count = word_search(data)
    print("Number of 'XMAS' occurrences:", XMAS_count)

if __name__ == '__main__':
    main()