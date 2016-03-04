#Charles Lynch
#Bubble Sort

class BubbleSort:

    def __init__(slef, list1):   # list1 takes a list as an argrment
        
        isRight = True

        x = sorted(list1)

        while isRight:
            for i in range (len(list1) - 1):   
                # if i index is greater than i + 1 
                if list1[i] > list1[i + 1]:  
                    # swaps index i with i + 1
                    list1[i + 1], list1[i] = list1[i], list1[i + 1]    
                    print (list1)
            if list1 == x:
                isRight = False

myList = [88, 98, 54, 35, 21, 22, 5, 9, 1]
BubbleSort(myList)