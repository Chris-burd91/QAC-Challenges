n = int(input("Please insert number:")) + 1


for i in range(1,n):
    for j in range(1,n):
        print("{:3}".format(i*j), end=" ")
    print()
n += 1