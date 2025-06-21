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



def trial_removal(levels):
    valid_levels_count = 0

    # Iterate through each level
    for level in levels:
        # Check level validity without removal
        if (calculate_validity(level)) == True:
            valid_levels_count += 1
            continue # Skip to next level
        
        # Check level validity removing one value at a time
        for i in range(len(level)):
                new_list = level[:i] + level[i+1:]
                if (calculate_validity(new_list)) == True:
                    valid_levels_count += 1
                    break # Break to next level

    return valid_levels_count


def calculate_validity(list):
    # Check all values increase or decrease
    if all(int(list[i]) < int(list[i + 1]) for i in range(len(list) - 1)) or \
        all(int(list[i]) > int(list[i + 1]) for i in range(len(list) - 1)):
        
        # Check sequential values differ by 1, 2, or 3
        if all(abs(int(list[i]) - int(list[i + 1])) in [1, 2, 3] for i in range(len(list) - 1)):
            return True
    return False


def main():
    filename = 'Day02/input.csv'
    levels = read_csv(filename)

    # Calculate the validity of each level
    valid_level_count = trial_removal(levels)

    # Print answer
    print("Number of valid levels:", valid_level_count)

if __name__ == '__main__':
    main()