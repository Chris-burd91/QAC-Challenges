def seven_not_five(x,y):
    numbers = []
    for i in range(x,y):
        if (i % 7 == 0) and (i % 5 != 0):
            numbers.append(i)
    return numbers

print(seven_not_five(2000,3201))