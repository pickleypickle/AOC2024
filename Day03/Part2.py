import re

def read_input(filename):
    # Read txt file into string
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return data
    
def calculate(data):
    # Add "do())" to the start of the string if it doesn't already exist
    if not data.startswith("do()"):
        data = "do()" + data

    # Split the string into segments where after every "don't()" a new segment starts but keep "don't()" in the text
    segments = re.split(r'(don\'t\(\))', data)

    # In each segment delete everything before the first "do()"
    segments = [segment[segment.find("do()"):] if "do()" in segment else segment for segment in segments]

    # If a segment does not contain "do()", remove it
    segments = [segment for segment in segments if "do()" in segment]

    # Find all instances of "mul(num,num)" in each segment
    mul_pattern = r'mul\((\d+),(\d+)\)'
    results = []
    for segment in segments:
        mul_matches = re.findall(mul_pattern, segment)
        for a, b in mul_matches:
            results.append(int(a) * int(b))

    return sum(results)


def main():
    data = read_input('Day03/input.txt')
    sum_result = calculate(data)

    print("Sum of products:", sum_result)

if __name__ == '__main__':
    main()