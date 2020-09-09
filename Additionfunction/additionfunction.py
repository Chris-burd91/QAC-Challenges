#def addition(input):
 #   a = input
  #  b = a + int(str(a)*2) + int(str(a)*3) + int(str(a)*4)
   # return y 

def aaaa(input, value):
   # input = "a+aa+aaa+aaaa"
    input = input.replace("a", str(value))
    input = input.split("+")
    for i in range(len(input)):
        input[i] = int(input[i])
    return sum(input)



