from hashlib import blake2b
from collections import Counter


class RemoveEvenInt:
    #This method has a return type of list and takes in param of list 
    def removeEInt(self,a:list) -> list:
        for i in a:
            if i % 2 == 0:
                a.remove(i)
                print("Value removed form list!")
        return a
        

    
    #This method has a return type of list and takes in param of list 
    
    def mergeSortedList(self,a:list,b:list) -> list:
        length_list_a = len(a)
        length_list_b = len(b)
        #If the last element in a is less than the first element in b then when merged a goes first
        if a[length_list_a-1] < b[0]:
            for x in b :
                a.append(x)  # two different way to add a list to another list 
            return a
        
        #If the last element in b is less than the first element in a then when merged b goes first
        if b[length_list_a-1] < a[0]:
            b.extend(a)      #two different way to add a list to another list
            return b

    def twoNumbers(self,a:list,b:int) -> list:
        #Select beginning value in list
        currentValue = 0
        constantlyChangingValue = 0
        target = b
        for i in range(0,len(a)-1):
            for j in range(1,len(a)-1):
                currentValue = a[i]          #This is the first Value in the List
                constantlyChangingValue = a[j] #This is the value that will be changing the most 
                if (currentValue + constantlyChangingValue) == target:
                    return [currentValue,constantlyChangingValue]
        return [-1]

    def minNum(self,a:list):
        length = len(a)
        if length <= 1:  #THis handles the base case of the function
            return a
        else:
            pivot = a.pop() #This gets the last value in the list and sets it to pivot

            items_greater = []
            items_lower = []

            for items in a:
                if items > pivot:
                    items_greater.append(items)
                else:
                    items_lower.append(items)
        final_list = self.minNum(items_lower) + [pivot]+ self.minNum(items_greater)
        new_list = final_list
        return [new_list[0]]
    

    def firstNonRepeatingValue(self,a:list) -> int :
        length = len(a)
        for i in range(0,length):
            for j in range(0,length):
                if i == j :
                    print("Value of i", i)
                    print("Value of j", j)

                    continue
                if a[i] == a[j]:
                    print("Value of a[i]", i)
                    print("Value of a[j]", j)
                    break
                else:
                    return a[i]
    
    def secondMaxValue(self,a:list):
        newSortedList = a.sort()  # THis sorts the list with a library function
        print("This is the sorted list: ", newSortedList)
        length = len(a)
        return a[length -2]
    

    def rightRotateList(self,a:list):
        length = len(a)

        #Create new list
        rotatedList = []
        #Take end of given list and place it at beginning index
        for x in range(length - 1 , length):
            rotatedList.append(a[x])
        #Shift the remanider of the indices to the right
        for i in range(0,length - 1):
            rotatedList.append(a[i])
            
        return rotatedList

    def rearrangeList(self,a:list):
        #Create two lists.
        positive_list = []
        negative_list = []
        output = []
        #Logic to seperate the outcomes
        for x in a:
            if x > 0:
                positive_list.append(x)
            else:
                negative_list.append(x)
        output = negative_list + positive_list
        return output
        

        



    
    



        




        






        
       
    

   
        

        
               
            
        




        

