#Charles Lynch
#Interest calculator

print ("Please enter requestid information.")

# get loan amount 
loanAmount = eval (input ("How much money would you like to borrow? : $"))

# get years of loan
loanTime = eval ( input ("How many years would you like loan for? :"))

# preset interest rate
interest = 5

# change loan years to months
payment = loanTime * 12

# change annual interest to monthly interest
monthly = interest / 1200

# calculate monthly payment
monthlyPayment = loanAmount * monthly / ( 1 - 1 / (1 + monthly) ** payment)
 
# calculate total payment
totalPayment = monthlyPayment * payment

print ("Interest Rate\t Monthly Payment\t Total Payment\t")
# while loop to print payments for each interest rate

while interest <= 8.0:
    print (str(interest) + "\t\t" + "$ " + str('%1.2f'% monthlyPayment) +\
        "\t\t" + "$ " + str('%1.2f'% totalPayment))
    interest = interest + .125
    monthly = interest / 1200
    monthlyPayment = loanAmount * monthly / ( 1 - 1 / (1 + monthly) ** payment)
    totalPayment = monthlyPayment * payment