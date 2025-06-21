import csv

def read_csv(filename):
    levels = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Split by spaces
            row = [elem.strip().split(' ') for elem in row]

            levels.extend(row)
    return levels

def calculate_validity(levels):
    valid_level_count = 0

    for level in levels:
        # Check all values increase or decrease
        if all(int(level[i]) < int(level[i + 1]) for i in range(len(level) - 1)) or \
           all(int(level[i]) > int(level[i + 1]) for i in range(len(level) - 1)):
           
           # Check sequential values differ by 1, 2, or 3
            if all(abs(int(level[i]) - int(level[i + 1])) in [1, 2, 3] for i in range(len(level) - 1)):
                valid_level_count += 1

    return valid_level_count

def main():
    filename = 'Day02/input.csv'
    levels = read_csv(filename)

    # Calculate the validity of each level
    valid_level_count = calculate_validity(levels)

    # Print answer
    print("Number of valid levels:", valid_level_count)

if __name__ == '__main__':
    main()