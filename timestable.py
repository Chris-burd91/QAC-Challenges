
def timestable():
  n = int(input("Please insert number:")) 
  for i in range(1,n+1):
      for j in range(1,n+1):
        print("{:4}".format(i*j), end="\t")
      print('\n')
   


timestable()







