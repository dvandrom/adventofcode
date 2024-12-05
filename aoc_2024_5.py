import re

#########
# Input #
#########
day=5
INPUT_FILE="/home/rsz-6139/PY/AdventOfCode/2024/aoc_2024_{}_input.txt".format(day)

#################
# Puzzle part 1 #
#################
"""
"""

####################
# Functions part 1 #
####################
def X_precedes_Y_in_Z(ruleXY,update_line_Z):
    # Split rule ruleXY in constituent parts X and Y
    ruleX=ruleXY.split("|")[0]
    ruleY=ruleXY.split("|")[1]

    # Regular expression pattern to check if 'X' precedes 'Y'
    pattern = '{}.*{}'.format(ruleX,ruleY)
    
    # Search for the pattern in the string 'update_line_Z'
    match = re.search(pattern, update_line_Z)
    
    # Return True if the pattern is found, otherwise False
    return bool(match)

def relevant_rule(rule,update_line):
    '''
    A rule is relevant for an update_line only if both pages mentioned in the rule appear in the update_line.
    Return: True or False
    '''
    if rule.split("|")[0] in update_line and rule.split("|")[1] in update_line:
        relevant = True
    else:
        relevant = False
    return bool(relevant)

################
# Solve part 1 #
################
input = open(INPUT_FILE,'r').read().split("\n\n")
#len(input) #2 OK

rules = input[0].splitlines()
#input[0].splitlines()[:5]
updates = input[1].splitlines()
#input[1].splitlines()[:5]
#len(rules)+len(updates)+1 #1374 OK = number of lines in INPUT_FILE

sum_middle_pages=0
for update_line in updates:
    #check whether all pages in the update_line adhere to all rules, if so sum middle page
    #--> do this by going over all rules X|Y and checking whether regexp(X-before-Y) holds for the update_line
    #--> ! however remember to only do this for rules that are relevant (i.e. X|Y in update_line)
    #NOTE also that this works only because all page numbers have two digits (otherwise 1|5 would be in 15,77 etc.)
    relevant_rules = [rule for rule in rules if relevant_rule(rule,update_line)]
    if all(X_precedes_Y_in_Z(rule,update_line) for rule in relevant_rules):
        lst_proper_order_pages = update_line.split(",")
        middle_page = lst_proper_order_pages[len(lst_proper_order_pages)//2]
        sum_middle_pages += int(middle_page)

answer = sum_middle_pages

# Solution to the puzzle
print("The solution to 2024 Day {} Part 1 is {}".format(day,answer))



#################
# Puzzle part 2 #
#################
"""
"""

####################
# Functions part 2 #
####################



################
# Solve part 2 #
################
input = open(INPUT_FILE,'r').read().split("\n\n")
#len(input) #2 OK

rules = input[0].splitlines()
#input[0].splitlines()[:5]
updates = input[1].splitlines()
#input[1].splitlines()[:5]
#len(rules)+len(updates)+1 #1374 OK = number of lines in INPUT_FILE

sum_middle_pages=0
i=0
for update_line in updates:
    #check whether all pages in the update_line adhere to all rules, if so sum middle page
    #--> do this by going over all rules X|Y and checking whether regexp(X-before-Y) holds for the update_line
    #--> ! however remember to only do this for rules that are relevant (i.e. X|Y in update_line)
    #NOTE also that this works only because all page numbers have two digits (otherwise 1|5 would be in 15,77 etc.)
    relevant_rules = [rule for rule in rules if relevant_rule(rule,update_line)]
    if not all(X_precedes_Y_in_Z(rule,update_line) for rule in relevant_rules):
        i += 1
        lst_wrong_order_pages = update_line.split(",")
        
        loop_rules = relevant_rules.copy()
        while not all(X_precedes_Y_in_Z(rule,update_line) for rule in loop_rules):
            lst_update_line = update_line.split(",")
            #take first relevant rule X1|Y1 and find all rules X|Y starting with X=X1
            first_rule = loop_rules[0]
            X1 = first_rule.split("|")[0]
            all_rules_X1 = [rule for rule in loop_rules if rule.split("|")[0]==X1]
            #consider all Y in rules with X=X1, find the lowest index of such Y in lst_wrong_order_pages
            all_rules_Y = [rule.split("|")[1] for rule in all_rules_X1]
            all_index_Y = [i for i,n in enumerate(lst_update_line) if n in all_rules_Y]
            low_index_Y = all_index_Y[0]
            #put X1 just in front of lowest index Y (in lst_update_line) 
            index_X1 = lst_update_line.index(X1) #first index of X1 in list (will be > low_index_Y)
            lst_update_line = lst_update_line[:low_index_Y]+[lst_update_line[index_X1]]+lst_update_line[low_index_Y:index_X1]+lst_update_line[index_X1+1:]
            #remove rules X1|Y from relevant rules (now adhered to)
            loop_rules = [loop_rule for loop_rule in loop_rules if loop_rule not in all_rules_X1]
            #NOTE that all(X_precedes_Y_in_Z(rule,update_line) for rule in []) returns True when loop_rules is empty

            lst_reordered_update_line = lst_update_line
            reordered_update_line = ",".join(lst_update_line) #lst of strings!
            update_line = reordered_update_line

        #now take middle element of lst_update_line to add to sum_middle_pages
        middle_page = lst_reordered_update_line[len(lst_reordered_update_line)//2]
        sum_middle_pages += int(middle_page)

        #
        if i<10:
            print(i)
            print("wrong order pages example:")
            print(lst_wrong_order_pages)
            print("relevant rules here:")
            print(relevant_rules)

            #After the while loop, the update_line should adhere to all rules
            print("Reordered update_line:")
            print(update_line)
            print("Does the reordered line adhere to all relevant_rules?")
            adherence = all(X_precedes_Y_in_Z(rule,update_line) for rule in relevant_rules)
            print(adherence)
            print("middle page number")
            print(middle_page)

    # Check for adherence now


answer = sum_middle_pages

# Solution to the puzzle
print("The solution to 2024 Day {} Part 2 is {}".format(day,answer))




#####################
# Development       #
# Edge case testing #
#####################

