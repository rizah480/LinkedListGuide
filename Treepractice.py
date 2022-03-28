#Node class created For Tree Data struct
from urllib.parse import non_hierarchical


class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

#Create Tree Data Struct
class Tree:
    def __init__(self,val = None):

        if val != None :
            self.val = val
        else:
            self.val = None
        
        self.right = None
        self.left = None
    
    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left == None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
            if val > self.val:
                if self.right == None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

#This is where the edge cases will be listed for this function
#The following Edge Cases have been dealt with for the delete()
#1 There is no value in tree that matches
#2 The value is larger than root tree value
#3 The value is smaller than root
#4 There is no node to replace node that has been deleted 



    
    def delete(self,val):
        tmp = Tree()
        if self.val:
            if val < self.val:
                if self.left == None:
                    print("There is nothing to delete")
                if self.left.val == val:
                    keeper = self.left
                    if keeper.left != None:
                        self.left = keeper.left
                    else:
                        self.left = Tree('x')
                else:
                    self.left.delete(val)
            
            if val > self.val:
                if self.right == None:
                    print("There is nothing to delete")
                if self.right.val == val:
                    coll = self.right
                    if coll.right != None:
                        self.right = coll.right
                    else:
                        self.right = Tree('x')
                else:
                    self.right.delete(val)
        else:
            print("The Tree does not have a value in its value spot")
    
    #This function is DEFECTIVE FOR NOW(FIX::TBD)
    def printValues(self):
        if self.left:
            self.left.printValues()
            
            print(self.val)
        if self.right:
            self.right.printValues()

        
        



#Begin implementation of Tree 

#Tree instance created

#Tree has been created and data has been properly stored inside



tree = Tree(6)
tree.right = Tree(7)
tree.insert(8)

print(tree.val)
print(tree.right.val)
print(tree.right.right.val)










