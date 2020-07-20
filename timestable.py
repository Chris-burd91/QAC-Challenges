
#def timestable():
 # n = int(input("Please insert number:")) 
  #for i in range(1,n+1):
   #   for j in range(1,n+1):
    #    print("{:3}".format(i*j), end="\t")
     # print('\n')

def timestable():
  n = int(input("Please insert number:")) 
  output = ""
  for i in range(1,n+1):
      for j in range(1,n+1):
        output += (str(i*j)) + "\t"
      output += "\n" + "\n"
  return output
   


print(timestable())







