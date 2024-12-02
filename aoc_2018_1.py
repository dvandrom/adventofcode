import numpy as np

# pylint: disable=pointless-string-statement
# pylint: disable=missing-function-docstring

"""
Script: aoc_2018_1.py

Today's puzzle (part 1)
-----------------------
    Starting with a frequency of zero, what is the resulting frequency after all of the changes 
    in frequency (given by the lines in input file 'aoc_2018_1_input.txt') have been applied?
"""


#########
# Input #
#########
INPUT_FILE="/home/userName/PY/AdventOfCode/2018/aoc_2018_1_input.txt"
TEST_FILE="/home/userName/PY/AdventOfCode/2018/test.txt"


##########################################################
# Tactic 1: Put Each Line of the File into a Numpy Array #
##########################################################

# Read file into a numpy array
def file_to_numpy_array(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        input_lines = np.array([line.strip() for line in file])
    return input_lines

# Usage
input_lines_array = file_to_numpy_array(INPUT_FILE)
print(input_lines_array[:5])


##########################################################
# Tactic 2: Execute my_function on Each Line of the File #
##########################################################

# Define a function to be executed on each line
def my_function(line):
    print(f"Processing: {line}")
    # Add custom logic here

# Execute function on each line
def process_file_lines(file_path, function):
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            function(line.strip())

# Usage
use_tactic2=False
if use_tactic2:
    process_file_lines(INPUT_FILE, my_function)


#############################
# Solve the puzzle - Part 1 #
#############################

# Define a function that parses input line strings to numeric values
def string_line_to_num(string_line):
    if string_line[0]=='-':
        out=-int(string_line[1:])
    elif string_line[0]=='+':
        out=int(string_line[1:])
    else:
        raise ValueError("The sign of the frequency adjustment is missing!")

    return out

# Usage
print("parsing input lines to numerics")
num_lines = np.array([string_line_to_num(line) for line in input_lines_array])
print(num_lines[:5])

# Solution to the puzzle
answer = np.sum(num_lines)
print("The solution to 2018 Day 1 Part 1 is ",answer)



#############################
# Solve the puzzle - Part 2 #
#############################
"""
Today's puzzle (Part 2)
-----------------------
    You notice that the device repeats the same frequency change list over and over.
    To calibrate the device, you need to find the first frequency it reaches twice.
    The input is the same.
"""

# Define a function to be executed on each line
#def my_function2(line):
    #print(f"Processing: {line}")
    # Add custom logic here

input_file=INPUT_FILE
#input_file=TEST_FILE

# Execute function on each line
i=0
j=0
array=[]
cum_array=[]
repeated_freq = 0
answer_found=False
while answer_found==False and j<100:
    j=j+1
    print("frequency period:",j)
    with open(input_file, mode='r', encoding='utf-8') as file:
        for line in file:
            i=i+1
            array.append(int(line))
            cum_sum=np.sum(np.asarray(array))
            if int(cum_sum) in cum_array and not answer_found:
                repeated_freq = cum_sum
                answer_found=True
            cum_array.append(int(cum_sum))
            if i<10:
                print("")
                print(i)
                print("freq update:", line)
                print("current freq:", cum_sum)
                print(array)
                print(cum_array)
            #my_function2(line.strip())

if answer_found:
    answer = repeated_freq
else:
    answer = 'not found!'

# Solution to the puzzle
print("The solution to 2018 Day 1 Part 2 is",answer)
