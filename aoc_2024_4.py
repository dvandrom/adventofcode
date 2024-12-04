#import re

#########
# Input #
#########
day=4
INPUT_FILE="/home/rsz-6139/PY/AdventOfCode/2024/aoc_2024_{}_input.txt".format(day)

#################
# Puzzle part 1 #
#################
"""
Find and count all instances of the word "XMAS" (horizontal, vertical, diagonal, written backwards, or even overlapping other words).
"""

####################
# Functions part 1 #
####################
def count_xmas_version1(lines):
    '''The first version implements the following strategy for each line of the imput file:
    - look for instances of 'XMAS' or 'SAMX';
    - if the line has at least three more consecutive lines in the input file, consider this batch of 4 lines in order to look for 'XMAS' or 'SAMX' vertically;
    - if the line has at least three more consecutive lines in the input file, consider this batch of 4 lines in order to look for 'XMAS' or 'SAMX' diagonally;
    '''
    word_set = {'XMAS', 'SAMX'}
    count = 0
    rows, cols = len(lines), len(lines[0])

    for i in range(rows):
        # Horizontal search
        for j in range(cols - 3):
            if lines[i][j:j + 4] in word_set:
                count += 1

        # Vertical and diagonal search (only if 3 more consecutive lines exist)
        if i <= rows - 4:
            for j in range(cols):
                # Vertical search
                vertical_word = ''.join([lines[i + k][j] for k in range(4)])
                if vertical_word in word_set:
                    count += 1

                # Diagonal search (both directions)
                if j <= cols - 4:  # Top-left to bottom-right
                    diagonal_word_lr = ''.join([lines[i + k][j + k] for k in range(4)])
                    if diagonal_word_lr in word_set:
                        count += 1
                if j >= 3:  # Top-right to bottom-left
                    diagonal_word_rl = ''.join([lines[i + k][j - k] for k in range(4)])
                    if diagonal_word_rl in word_set:
                        count += 1

    return count

def count_xmas_version2(lines):
    '''This version treats the grid as a matrix and uses a unified sliding window to search for horizontal, vertical, and diagonal occurrences in a single pass.
    The sliding window approach for all directions in a single loop makes the logic slightly more concise.
    '''
    word_set = {'XMAS', 'SAMX'}
    count = 0
    rows, cols = len(lines), len(lines[0])

    for i in range(rows):
        for j in range(cols):
            # Horizontal search
            if j <= cols - 4:
                horizontal_word = ''.join(lines[i][j:j + 4])
                if horizontal_word in word_set:
                    count += 1

            # Vertical search
            if i <= rows - 4:
                vertical_word = ''.join(lines[i + k][j] for k in range(4))
                if vertical_word in word_set:
                    count += 1

            # Diagonal search (Top-left to bottom-right)
            if i <= rows - 4 and j <= cols - 4:
                diagonal_word_lr = ''.join(lines[i + k][j + k] for k in range(4))
                if diagonal_word_lr in word_set:
                    count += 1

            # Diagonal search (Top-right to bottom-left)
            if i <= rows - 4 and j >= 3:
                diagonal_word_rl = ''.join(lines[i + k][j - k] for k in range(4))
                if diagonal_word_rl in word_set:
                    count += 1

    return count


################
# Solve part 1 #
################
input_lines = [line.strip() for line in open(INPUT_FILE, 'r')]

# Using count_xmas_version1
answer_version1 = count_xmas_version1(input_lines)
print("Version 1 Count:", answer_version1)

# Using count_xmas_version2
answer_version2 = count_xmas_version2(input_lines)
print("Version 2 Count:", answer_version2)

# Solution to the puzzle
if answer_version1 == answer_version2:
    answer=answer_version1
print("The solution to 2024 Day {} Part 1 is {}".format(day,answer))



#################
# Puzzle part 2 #
#################
"""
Find and count all instances of a pattern 'X-MAS'. 
A pattern is a valid 'X-MAS' pattern if it contains the words 'MAS' or 'SAM' diagonally crossed
(note: the pattern is only valid if 'MAS' or 'SAM' appear on both diagonals).
"""

####################
# Functions part 2 #
####################
def count_xmas_pattern(lines):
    pattern_set = {'MAS', 'SAM'}
    count = 0
    rows, cols = len(lines), len(lines[0])

    for i in range(rows - 2):  # Sliding 3x3 window vertically
        for j in range(cols - 2):  # Sliding 3x3 window horizontally
            # Extracting the 3x3 window
            window = [
                [lines[i + x][j + y] for y in range(3)]
                for x in range(3)
            ]

            # Checking for 'MAS' or 'SAM' in both diagonals
            diagonal_lr = window[0][0] + window[1][1] + window[2][2]  # Top-left to bottom-right
            diagonal_rl = window[0][2] + window[1][1] + window[2][0]  # Top-right to bottom-left

            if diagonal_lr in pattern_set and diagonal_rl in pattern_set:
                count += 1

    return count


################
# Solve part 2 #
################
input_lines = [line.strip() for line in open(INPUT_FILE, 'r')]
answer = count_xmas_pattern(input_lines)
print("Count of valid X-MAS patterns:", answer)

# Solution to the puzzle
print("The solution to 2024 Day {} Part 2 is {}".format(day,answer))




#####################
# Development       #
# Edge case testing #
#####################

