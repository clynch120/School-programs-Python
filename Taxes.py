#Charles Lynch
#Tax table 6.15

# function to output taxes to pay based on income
def computeTax(status, income = 50000):
    # output of single status and married separate (they are in the same tax bracket)
    if status == "single" or "marriedSeparate":
        startTax = 8675.5
        for i in range (income, 60001, 50): # print and add tax rate
            startTax += 12.5
            print (i, end = '' "\t")
            print ('%1.1f'% startTax)
    # output of married joint status
    elif status == "marriedJoint":
        startTax = 6657.538
        for i in range (income, 60001, 50):
            startTax += 7.5
            print (i, end = '' "\t")
            print ('%1.0f'% startTax)
    # output of head of house (use any parmanter to print hoh)
    else:
        startTax = 7339.5
        for i in range (income, 60001, 50):
            startTax += 12.5
            print (i, end = '' "\t")
            print ('%1.0f'% startTax)

# call the function computeTax
computeTax("marriedJoint")