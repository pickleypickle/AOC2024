import re

def read_input(filename):
    # Read txt file into string
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return data
    
def calculate(data):
    # Identify part of the string that match the format "mul(num,num)" and no others
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)

    # Take the identified sections and multiply the two numbers together then sum
    results = [int(a) * int(b) for a, b in matches]
    
    return sum(results)

def main():
    data = read_input('Day03/input.txt')
    sum_result = calculate(data)

    print("Sum of products:", sum_result)

if __name__ == '__main__':
    main()