#Python Write a function that accepts a sequence of whitespace separated words as a string input,
#  sorts each item alphanumerically and removes any duplicate items, then returns the result as a string. Write a test for this function.

 #Suppose the following input is supplied to the program:
 #  hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world

 
#Hint: make use of the set() collection type!

def setstring(input):
    convert_list = input.split()
    convert_set = set(convert_list)
    sort_set = sorted(convert_set)
    convert_back = [str(s) for s in sort_set]
    joined_string = " ".join(convert_back)
    #convert_set.sort()
        

    return joined_string
print(setstring("why hello cabbage goodbye basketball"))
