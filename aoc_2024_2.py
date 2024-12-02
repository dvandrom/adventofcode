from collections import Counter

#########
# Input #
#########
day=2
INPUT_FILE="/home/userName/PY/AdventOfCode/2024/aoc_2024_{}_input.txt".format(day)

#################
# Puzzle part 1 #
#################
"""
The unusual data (your puzzle input) consists of many reports, one report per line.
Each report is a list of numbers called levels that are separated by spaces.
The engineers are trying to figure out which reports are safe.
A report only counts as safe if both of the following are true:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
How many reports are safe?
"""

####################
# Functions part 1 #
####################
def fun_report_as_list(line):
    return([int(level) for level in line.split(sep=" ")])

def fun_report_increments(report_line):
    return([report_line[i+1]-report_line[i] for i in range(len(report_line)-1)])

def fun_report_safe(report_incrs):
    l_monotonous_incrs=0 #assume level increments are not monotonous
    str_monotony_type="not monotonous"
    if all(incr>0 for incr in report_incrs):
        str_monotony_type="ascending"
    if all(incr<0 for incr in report_incrs):
        str_monotony_type="descending"
    if str_monotony_type=="ascending" or str_monotony_type=="descending":
        l_monotonous_incrs=1 #set to 1 if monotonous level increments
    l_safe_increment_sizes=0 #assume unsafe level increments
    if all(abs(int(incr)) < 4 for incr in report_incrs):
        l_safe_increment_sizes=1 #set to 1 if safe level increments
    l_report_safe=0 #assume report of this line is not safe
    if l_monotonous_incrs==1 and l_safe_increment_sizes==1:
        l_report_safe=1 #set report to safe if level increments safe and monotonous
    return l_report_safe,l_safe_increment_sizes,l_monotonous_incrs,str_monotony_type

################
# Solve part 1 #
################
with open(INPUT_FILE, mode='r', encoding='utf-8') as file:
    i=0
    lis_l_report_safe=[] #list of 0/1 dep. on l_report_safe
    for line in file:
        i=i+1
        lis_report_line=fun_report_as_list(line.strip())
        lis_report_incr=fun_report_increments(lis_report_line)
        l_report_safe,l_safe_increment_sizes,l_monotonous_incrs,str_monotony_type=fun_report_safe(lis_report_incr)
        str_safe="Unsafe"
        if l_report_safe==1:
            str_safe="Safe"
        str_incr="Increments exceed bounds"
        if l_safe_increment_sizes==1:
            str_incr="Increments within bounds"
        lis_l_report_safe.append(l_report_safe)
        #
        if i<10:
            print("{} Report line:\t     {}".format(i,lis_report_line))
            print("  Report increments: {}".format(lis_report_incr))
            print("  The report levels are {}:\t {}\t{}".format(str_safe,str_monotony_type,str_incr))
# Some checks
len(lis_l_report_safe)

# Solution to the puzzle
answer = sum(lis_l_report_safe)
print("The solution to 2024 Day {} Part 1 is {}".format(day,answer))



####################
# Functions part 2 #
####################
def fun_report_safe_with_damp(lis_report_line):
    # Iterate over the report line, omitting 1 report level and checking for safety
    l_report_safe=0
    k_level_to_remove=None
    for k in range(len(lis_report_line)):
        if l_report_safe==0: #only do this if it is still necessary
            #report_line with the k'th level removed 
            report_line=lis_report_line[:k] + lis_report_line[(k + 1):]
            #corresponding increments
            report_incrs=fun_report_increments(report_line)
            #now check the Safety
            new_report_safe,_,_,_=fun_report_safe(report_incrs)
            if new_report_safe==1:
                l_report_safe=1
                k_level_to_remove=k+1 #because k is an index starting at 0

    return l_report_safe,k_level_to_remove

def fun_str_kth(k):
    "Use only on integer k >= 1."
    if k==1:
        str_kth = str(k)+"st"
    elif k==2:
        str_kth = str(k)+"nd"
    elif k==3:
        str_kth = str(k)+"rd"
    else:
        str_kth = str(k)+"th"
    return(str_kth)

################
# Solve part 2 #
################
with open(INPUT_FILE, mode='r', encoding='utf-8') as file:
    i=0
    lis_l_report_safe=[] #list of 0/1 dep. on l_report_safe
    for line in file:
        i=i+1
        lis_report_line=fun_report_as_list(line.strip())
        lis_report_incr=fun_report_increments(lis_report_line)
        l_report_safe,l_safe_increment_sizes,l_monotonous_incrs,str_monotony_type=fun_report_safe(lis_report_incr)
        str_safe="Unsafe"
        if l_report_safe==1:
            str_safe="Safe"
        str_incr="Increments exceed bounds"
        if l_safe_increment_sizes==1:
            str_incr="Increments within bounds"
        # PART2 LOGIC
        if l_report_safe==0:
            #iterate over the report line, omitting 1 report level and checking for safety
            l_report_safe,k_level_to_remove=fun_report_safe_with_damp(lis_report_line)
            if l_report_safe==1:
                str_level_to_remove = fun_str_kth(k_level_to_remove)
        lis_l_report_safe.append(l_report_safe)
        # DISPLAY
        if i<10:
            print("{} Report line:\t     {}".format(i,lis_report_line))
            print("  Report increments: {}".format(lis_report_incr))
            print("  The report levels are {}:\t {}\t{}".format(str_safe,str_monotony_type,str_incr))
            if str_safe=="Unsafe" and l_report_safe==1:
                print("  Report line made safe by removing {} level".format(str_level_to_remove))

# Some checks
len(lis_l_report_safe)
Counter(lis_l_report_safe) #{1: 536, 0: 464}
sum(lis_l_report_safe) #536

# Solution to the puzzle
answer = sum(lis_l_report_safe)
print("The solution to 2024 Day {} Part 2 is {}".format(day,answer))



######################
# OBSOLETE FROM HERE #
######################
"""
My first try of a solution tried to avoid iterating over the levels of each report.
It tried to consider the patterns in level increments.
However, counting the nr of breaches in pattern does not guarantee, if the nr is 1,
that the resulting pattern when removing 1 element is conform to reactor safety.
My first try forgot to re-test this.
"""

#################
# Puzzle part 2 #
#################
"""
The Problem Dampener is a reactor-mounted module that lets the reactor safety systems 
tolerate a single bad level in what would otherwise be a safe report.
How many reports are now safe?
"""

####################
# Functions part 2 #
####################
def parse_report(report_line_incrs):
    #the idea is to have this function discern what the problem is, in this order:
    # line with one zero, then give index of that zero
    # line with more than one zero --> not salvagable
    # (asc) line with mostly positives but 1 negative, then give index of the negative
    #                                  but >1 negative --> not salvagable
    # (desc) line with mostly negatives but 1 positive, then give index of positive
    #                                   but >1 positive --> not salvagable
    #may be adapted to return
    # nr_zeroes, zero_index (index if 1; None if multiple)
    # ascending (1/0), lis_exception_index, exception_index (index if 1; None if multiple)
    #returns:
    # l_safe (1/0), nr_zeroes, nr_exceptions

    #zero_index=None
    report_line_counter=Counter(report_line_incrs)
    nr_zeroes=report_line_counter[0]
    #if nr_zeroes==1:
    #    zero_index=report_line_incrs.index(0)

    #exception_index=None
    pos_index = [i for i,n in enumerate(report_line_incrs) if n > 0]
    nr_pos_incr = len(pos_index)
    neg_index = [i for i,n in enumerate(report_line_incrs) if n < 0]
    nr_neg_incr = len(neg_index)
    if nr_pos_incr >= nr_neg_incr:
        ascending=1
        lis_exception_index=neg_index.copy()
        nr_exceptions=len(lis_exception_index)
    if nr_neg_incr > nr_pos_incr:
        ascending=0
        lis_exception_index=pos_index.copy()
        nr_exceptions=len(lis_exception_index)
    #if nr_exceptions==1:
    #    exception_index=lis_exception_index[0]

    l_safe = 0 #assume the report line indicates Unsafe levels
    if nr_zeroes+nr_exceptions <= 1:
        l_safe = 1 #set to Safe if at most 1 bad level has to be tolerated

    return l_safe, nr_zeroes, nr_exceptions

################
# Solve part 2 #
################
with open(INPUT_FILE, mode='r', encoding='utf-8') as file:
    i=0
    lis_lis_report_line=[] #list with each report line as a list of levels
    lis_lis_report_incr=[] #list with for each report line list of level increments
    for line in file:
        i=i+1
        lis_report_line=fun_report_as_list(line.strip())
        lis_report_incr=fun_report_increments(lis_report_line)
        lis_lis_report_line.append(lis_report_line)
        lis_lis_report_incr.append(lis_report_incr)
        #if i<10:
        #    print("{} Report line:\t     {}".format(i,lis_report_line))
        #    print("  Report increments: {}".format(lis_report_incr))

# Some checks
len(lis_lis_report_line)
len(lis_lis_report_incr)
lis_lis_report_line[0]
lis_lis_report_incr[0]

lis_l_safe = []
lis_nr_zeroes = []
lis_nr_exceptions = []
for lis_report_incr in lis_lis_report_incr:
    l_safe, nr_zeroes, nr_exceptions=parse_report(lis_report_incr)
    lis_l_safe.append(l_safe)
    lis_nr_zeroes.append(nr_zeroes)
    lis_nr_exceptions.append(nr_exceptions)
# Some checks
len(lis_l_safe)
len(lis_nr_zeroes)
len(lis_nr_exceptions)
Counter(lis_nr_zeroes) #Counter({0: 750, 1: 196, 2: 50, 3: 4})
Counter(lis_nr_exceptions) #Counter({0: 748, 1: 204, 2: 45, 3: 3})
Counter(lis_l_safe) #Counter({1: 819, 0: 181})
sum(lis_l_safe) #819

# Solution to the puzzle
answer = sum(lis_l_safe)
print("The solution to 2024 Day {} Part 2 is {}".format(day,answer))
