#Charles Lynch
#Playing with numbers 6.3

def reverse (num):
    print ( str(num)[ : : -1])
    

def ispalindrome (num):
    i= str(num)[::-1]
    print( str(num) == i)

reverse(4321)
ispalindrome(121)
input()