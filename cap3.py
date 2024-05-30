################################
# Github Repo link
# Tika Devi Adhikari
# Your Section 
# Your Student ID Number
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score: <total sum>
################################


def read_input(file_name):
    """
    Reads lines from the given input file.

    :param file_name: Name of the input file.
    :return: List of strings where each string is a line from the file.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def extract_number(line):
    """
    Extracts the two-digit number from a given line.
    The number is formed by the first and last digits in the line.

    :param line: A single line of input.
    :return: An integer formed by the first and last digit.
    """
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0  # In case there are no digits, which shouldn't be a valid scenario based on problem description.

def print_solution(file_name):
    """
    Reads the input file, processes the lines to compute the required sum,
    and prints the solution in the specified format.

    :param file_name: Name of the input file.
    """
    lines = read_input(file_name)
    total_sum = 0

    for line in lines:
        number = extract_number(line.strip())
        total_sum += number

    print(f"The total sum from the 362.txt file {file_name} is {total_sum}")

# Replace 'input.txt' with the actual name of your input file
input_file_name = '362.txt'
print_solution(input_file_name)
