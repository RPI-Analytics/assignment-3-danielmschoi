def divby2(x):
    temp = []
    for i in range(len(x)):
        if (x[i]%2 == 0):
            temp.append(x[i])
    return temp