import re

#########
# Input #
#########
day=3
INPUT_FILE="/home/rsz-6139/PY/AdventOfCode/2024/aoc_2024_{}_input.txt".format(day)

#################
# Puzzle part 1 #
#################
"""
It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

####################
# Functions part 1 #
####################
def extract_and_multiply(input_string):
    # Regular expression to find all occurrences of "mul(X,Y)" where X and Y are 1 to 3 digit numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    # Initialize the sum
    total_sum = 0
    
    # Iterate over all matches
    for match in matches:
        # Extract X and Y from the match and convert them to integers
        x, y = int(match[0]), int(match[1])
        
        # Multiply X and Y and add to the total sum
        total_sum += x * y
    
    return total_sum

################
# Solve part 1 #
################
# Read the contents of the file as one string
with open(INPUT_FILE, 'r') as file:
    input_string = file.read()

# Calculate the sum of all multiplications
result = extract_and_multiply(input_string)

# Solution to the puzzle
print("The solution to 2024 Day {} Part 1 is {}".format(day,result))


#################
# Puzzle part 2 #
#################
"""
There are two new instructions you'll need to handle:
- The do() instruction enables future mul instructions.
- The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies.
At the beginning of the program, mul instructions are enabled.
"""

####################
# Functions part 2 #
####################
def extract_and_multiply_with_conditions(input_string):
    # Split the input string by "don't()"
    segments = input_string.split("don't()")
    
    # Initialize the sum
    total_sum = 0
    
    # Regular expression to find all occurrences of "mul(X,Y)" where X and Y are 1 to 3 digit numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    for i, segment in enumerate(segments):
        # Treat first segment, enabled even without "do()"" 
        if i == 0:
            # Find all matches in the segment
            matches = re.findall(pattern, segment)
            
            # Iterate over all matches
            for match in matches:
                # Extract X and Y from the match and convert them to integers
                x, y = int(match[0]), int(match[1])
                
                # Multiply X and Y and add to the total sum
                total_sum += x * y
        
        # Treat any segment that may follow a "don't()" occurrence
        else:
            subsegments = segment.split("do()")
            
            for j, subsegment in enumerate(subsegments):
                # Ignore the first subsegment, since it follows a "don't()" and precedes a "do()"
                if j > 0:
                    # Iterate over all matches in subsegment
                    for submatch in re.findall(pattern, subsegment):
                        # Extract X and Y from the submatch and convert them to integers
                        x, y = int(submatch[0]), int(submatch[1])
                        
                        # Multiply X and Y and add to the total sum
                        total_sum += x*y
    
    return total_sum

################
# Solve part 2 #
################
# Read the contents of the file as one string
with open(INPUT_FILE, 'r') as file:
    input_string = file.read()

# Calculate the sum of all multiplications
result = extract_and_multiply_with_conditions(input_string)

# Solution to the puzzle
print("The solution to 2024 Day {} Part 2 is {}".format(day,result))




#####################
# Development       #
# Edge case testing #
#####################

def extract_and_multiply_with_conditions(input_string):
    # Split the input string by "don't()"
    segments = input_string.split("don't()")
    
    # Initialize the sum
    total_sum = 0
    
    # Regular expression to find all occurrences of "mul(X,Y)" where X and Y are 1 to 3 digit numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    for i, segment in enumerate(segments):
        # Treat first segment, enabled even without "do()"" 
        if i == 0:
            # Find all matches in the segment
            matches = re.findall(pattern, segment)
            
            # Iterate over all matches
            for match in matches:
                # Extract X and Y from the match and convert them to integers
                x, y = int(match[0]), int(match[1])
                
                # Multiply X and Y and add to the total sum
                total_sum += x * y
        
        # Treat any segment that may follow a "don't()" occurrence
        else:
            subsegments = segment.split("do()")
            
            for j, subsegment in enumerate(subsegments):
                # Ignore the first subsegment, since it follows a "don't()" and precedes a "do()"
                if j > 0:
                    # Iterate over all matches in subsegment
                    for submatch in re.findall(pattern, subsegment):
                        # Extract X and Y from the submatch and convert them to integers
                        x, y = int(submatch[0]), int(submatch[1])
                        
                        # Multiply X and Y and add to the total sum
                        total_sum += x*y
    
    return total_sum

# Input string for edge case testing 
input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input_string = "don't()do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
#etc.

# Calculate the sum of all multiplications
result = extract_and_multiply_with_conditions(input_string)

print(f"The sum of all multiplications is: {result}")
