from collections import Counter

#########
# Input #
#########
INPUT_FILE="/home/userName/PY/AdventOfCode/2024/aoc_2024_1_input.txt"

#################
# Puzzle part 1 #
#################
"""The Historians split into two groups, each searching the office and trying to create
their own complete list of location IDs.
There's just one problem: by holding the two lists up side by side (your puzzle input), 
it quickly becomes clear that the lists aren't very similar.
To find out, pair up the numbers and measure how far apart they are. Pair up the smallest 
number in the left list with the smallest number in the right list, then the second-smallest 
left number with the second-smallest right number, and so on.
Within each pair, figure out how far apart the two numbers are.
To find the total distance between the left list and the right list, 
add up the distances between all of the pairs you found.
What is the total distance between your lists?
"""

####################
# Functions part 1 #
####################
def get_left_loc(line):
    return(line[0:5])

def get_right_loc(line):
    return(line[8:13])

def diff_loc(index):
    return(abs(int(left_list[index])-int(right_list[index])))

################
# Solve part 1 #
################
with open(INPUT_FILE, mode='r', encoding='utf-8') as file:
    i=0
    left_list=[]
    right_list=[]
    for line in file:
        i=i+1
        left=get_left_loc(line.strip())
        right=get_right_loc(line.strip())
        left_list.append(left)
        right_list.append(right)
        #if i<10:
        #    print("i\tleft_loc: '{}'\tright_loc: '{}'".format(left,right))

left_list.sort(reverse=False) #default list.sort(reverse=False) means ascending
right_list.sort(reverse=False)

#print(left_list[:5])
#print(right_list[:5])

diff_list = [diff_loc(j) for j in range(len(left_list))]
#len(left_list)
#len(right_list)
#len(diff_list)
#diff_list[:5]

# Solution to the puzzle
answer = sum(diff_list)
print("The solution to 2024 Day 1 Part 1 is ",answer)


#################
# Puzzle part 2 #
#################
"""
Calculate a total similarity score by adding up each number in the left list after 
multiplying it by the number of times that number appears in the right list.
"""

####################
# Functions part 2 #
####################
# a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
# res = Counter(a) #from collections import Counter
# print(res[3]) #Get count of 3

################
# Solve part 2 #
################
# Counter object with Frequency of locations in right list
ctr_freq_in_right = Counter(right_list)
# Similarity score of a location = location*(Freq of that location in right list)
lis_left_similarity_in_right = [int(left_loc)*ctr_freq_in_right[left_loc] for left_loc in left_list]
# Total similarity score
int_similarity_score = sum(lis_left_similarity_in_right)

# Solution to the puzzle
print("The solution to 2024 Day 1 Part 2 is ",int_similarity_score)

