import unittest
from rEvenInt import RemoveEvenInt # This is how you properly import a file(module) and a class inside of it
class Test_Week1(unittest.TestCase):


    #This is an example test case written in python 
    def testFirstTestWeek1(self):
        self.assertEqual(0,0)



    #This is the first Real test.......REMOVING EVEN INTEGERS FROM A LIST 

    def testRemoveEvenIntegers(self):
        t_r_e = RemoveEvenInt()
        test_list = [1,2,3,4,5,6,7,8,9]
        expectedResult = [1,3,5,7,9]
        actualResult = t_r_e.removeEInt(test_list)
        print("These are the results of this test case: ", t_r_e.removeEInt(test_list) )
        self.assertEqual(expectedResult,test_list)
    

    # This is a test to merge two sorted list into one list

    def testMergeTwoSortedList(self):
        t_r_e = RemoveEvenInt()
        test_list1 = [1,2,3,4,5]
        test_list2 = [6,7,8,9,10]
        expectedResult = [1,2,3,4,5,6,7,8,9,10]
        actualResult = t_r_e.mergeSortedList(test_list1,test_list2)
        self.assertEqual(expectedResult,actualResult)

    def testTwoNumbersThatAddToK(self):
        t_r_e = RemoveEvenInt()
        expectedResult = [3,4] # This is in the case that the value we are looking for is Seven 
        test_list1 = [20,3,4,5,6,8,9,10]
        actualResult = t_r_e.twoNumbers(test_list1,7)
        self.assertEqual(expectedResult,actualResult)
    
    def testTwoNumbersThatAddToKValueIsntThere(self):
        t_r_e = RemoveEvenInt()
        expectedResult = [-1] # This is in the case that the value we are looking for is not present.
        test_list1 = [20,3,4,5,6,8,9,10]
        actualResult = t_r_e.twoNumbers(test_list1,1100)
        self.assertEqual(expectedResult,actualResult)
    
    def testMinimumValueInTheList(self):
        #This will be using QuickSort
        t_r_e = RemoveEvenInt()
        expectedResult = [1]
        list_value = [12,3,4,5,4,3,4,6,7,8,6,5,7,8,1]
        actualResult = t_r_e.minNum(list_value)

        self.assertEqual(expectedResult,actualResult)
    
    def testFirstNonRepeatingInteger(self):
        t_r_e = RemoveEvenInt()
        expectedResult = 13
        listValue = [13,2,4,3,4,5,6,3,3,4,5,6,3,8]
        actualResult = t_r_e.firstNonRepeatingValue(listValue)
        self.assertEqual(expectedResult,actualResult)

    
    def testSecondMaximumValueInList(self):
        t_r_e = RemoveEvenInt()
        expectedResult = 8 # seond largest number will go here
        list_value = [9, 3, 3, 6, 8, 5, 4, 6, 3, 7]
        actualResult = t_r_e.secondMaxValue(list_value)
        self.assertEqual(expectedResult,actualResult)

    def testRightRotateList(self):
        t_r_e = RemoveEvenInt()
        expectedResult = [5,1,2,3,4]
        list_value = [1,2,3,4,5]
        actualResult = t_r_e.rightRotateList(list_value)
        self.assertEqual(expectedResult,actualResult)

    def testRearrangeList(self):
        t_r_e = RemoveEvenInt()
        list_value = [6,-1,7,-2,-3,8,9,10,-4,-5]
        expectedResult = [-1,-2,-3,-4,-5,6,7,8,9,10]
        actualResult = t_r_e.rearrangeList(list_value)
        self.assertEqual(expectedResult,actualResult)





    




    


        
        



if __name__ == '__main__':
    unittest.main()