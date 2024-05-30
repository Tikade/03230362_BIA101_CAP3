################################
# Github Repo link
# Tika Devi Adhikari
#BBI "H"
# 03230362
################################
# REFERENCES
#https://youtu.be/k9TUPpGqYTo?si=xIfjYzaB7ZOK3wRj
#https://youtu.be/7R6Ji8s-vVI?si=9pkQSu_d2uQtX8hd
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
        #read all lines from file and store them in list
        lines = file.readlines()
   #return all the list from the line
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
       #check if the character is a digit or not 
        if char.isdigit():
            # if the first digit is not, set it to the current digit 
            if first_digit is None:
                first_digit = char
            #update last digit to the current digit 
            last_digit = char
    
    #if both first digit were not found
    if first_digit is not None and last_digit is not None:
       #combine them to a two digit and return as integer 
        return int(first_digit + last_digit)
    else:
      # return 0 if in case there are no digits in a line.(if line contain only alphabates)  
        return 0

def print_solution(file_name):
    """
    Reads the input file, processes the lines to compute the required sum,
    and prints the solution in the specified format.

    :param file_name: Name of the input file.
    """
    lines = read_input(file_name)
    total_sum = 0 

    print("Line-wise extracted numbers:")
    for i, line in enumerate(lines):
        number = extract_number(line.strip())
        total_sum += number
        print(f"Line {i+1}: {number}")

   #print the final total sum 
    print(f"The total sum from the given input file {file_name} is {total_sum}")

input_file_name = '362.txt'

print_solution(input_file_name)
