#for getting secruity error
#set-executionpolicy remotesigned



"""
   Properties:
   1. Indexing           (list,tuple)
   2. Negative Indexing  (list,tuple)
   3. Slicing            (list,tuple,dict)
   4. Concatenation      (list,)
   5. Multiplicity       (list,)
   6. Membership testing (list,tuple,set,dict{on keys only})
   
 IF my_data IS DICTIONARY
print(len(my_data))
print(min(my_data))
print(max(my_data))
print(sum(my_data)) # -> works only for int keys
   ** key cannot be altered in dict , only values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
args make tuple; kwargs make dictionary

** Append can add only item at last, insert function is to add item in between 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# C = A + B
# print("C is:", C)     # Error

D = A - B         
print("D is:", D)      remove common elements from A @output= {1,2,3}

E = A ^ B
print("E is:", E)       remove common elements in both @output = {1,2,3,6,7,8}

F = A | B
print("F is:", F)      add elements with uniqueness @ouptu = {1,2,3,4,5,6,7,8}

G = A & B              gives common elements in A and B   @output {4,5}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~
   
   
   
   
"""
