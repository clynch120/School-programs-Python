#Charles Lynch
#Future Investments 6.7

def future():
    a = eval( input ("Investment amount : "))
    b = eval( input ("Annual interest : "))
    print ("Years \t Future Value ")
    j = (b / 100) / 12
    for i in range(1, 31):

        c = a * (1 + j) ** (i * 12)
        print (str(i) + "\t " + "$" + str('%1.2f'%c))

future()