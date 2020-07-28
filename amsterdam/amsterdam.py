import re

def amsterdam(string, word):
    string = string.lower()
    return len(re.findall(r'\b{}\b'.format(word),string))

   


        

        
