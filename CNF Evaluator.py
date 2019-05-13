#This program takes formulas in conjunctive normal form, goes through all
#interpretations of the formula, and outputs whether the formula is
#satisfiable, logically valid, or unsatisfiable as well as the truth values for each interpretation of the formula.

number_conjuncts = eval(input("Enter the number of conjuncts within the formula: "))

print("Now for each disjunctive clause, enter the terms within the disjunctive clause 'K1,~K2,K3,etc.'")
print("Separate each term with a space.")

x = 1           #Count for the disjunct while loop
total_disjunct_list = []
while x <= number_conjuncts:
    print("Disjunct ", end ='')
    print(x, end='')
    print(": ", end='')
    input_string = input()
    disjunct_list = input_string.split()
    total_disjunct_list.append(disjunct_list)
    x += 1

                #Construction of list containing every term, keeping negations, with duplicates, in formula: 'term_list'

term_list = []
x = 0           #Count for outer-loop
y = 0           #Count for inner-loop
while x < number_conjuncts:
    disjunct = total_disjunct_list[x]
    while y < len(disjunct):
        term_list.append(disjunct[y])
        y += 1
    x += 1
    y = 0

                #Removing duplicates and negation operators from term_list to make: 'term_set'

x = 0           #Count for loop to remove negation operators
while x < len(term_list):
    y = term_list[x]
    if y.find('~') != -1:
        y = y.replace('~','')
        term_list.remove(term_list[x])
        term_list.append(y)
    x += 1
term_set = list(set(term_list))
term_set.sort()

                #Start creating interpretations for the formula

x = 0           #Count representing each interpretation
y = 0           #Count for picking elements out of total_disjunct_list
z = 0           #Count for picking elements out of term_set
w = 0           #Count for picking elements out of particular disjuncts
i = 0           #Extra Count
conjunct_truth_list = []
truth_list = []
disjunct_truth_list = []
meta_truth_list = []
while x < 2**len(term_set):
    while z < len(term_set):                            #The while loop assigning truth values to each term for each x
        bool_determine1 = 2**(len(term_set)-(z+1))      
        bool_determine2 = x//bool_determine1
        bool_determine3 = bool_determine2 % 2
        if bool_determine3 == 0:
            truth_list.append(True)
        else:
            truth_list.append(False)
        z += 1
    while y < len(total_disjunct_list):                 #Loop evaluating truth value of each disjunctive clause
        disjunct = total_disjunct_list[y]
        while w < len(disjunct):
            term = disjunct[w]
            while i < len(term_set):
                if term == term_set[i]:
                    disjunct_truth_list.append(truth_list[i])
                elif term.replace('~','') == term_set[i]:
                    disjunct_truth_list.append(not truth_list[i])
                i += 1
            w += 1
            i = 0
        if disjunct_truth_list.count(True) > 0:         #Building list of the truth values of each conjunct (disjunctive clause)
            conjunct_truth_list.append(True)
        else:
            conjunct_truth_list.append(False)
        w = 0
        disjunct_truth_list = []
        y += 1
    if conjunct_truth_list.count(False) == 0:           #Determining truth value of entire formula for x
        meta_truth_list.append(True)                    #Appending truth value to list containing truth values for each interpretation
    else:
        meta_truth_list.append(False)
    y = 0
    z = 0
    truth_list = []
    x += 1
    conjunct_truth_list = []

print("The possible truth values of the formula:")

print(meta_truth_list)                                  #Printing every possible truth value of the formula

if (meta_truth_list.count(False) == 0):                 #Printing whether formula is "Valid," "Satisfiable," or "Unsatisfiable"
    print("Logically Valid")
elif (meta_truth_list.count(True) > 0):
    print("Satisfiable")
else:
    print("Unsatisfiable")
                
        
            
            
        
            
        
    

    
    
    
