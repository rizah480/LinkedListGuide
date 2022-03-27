#Node class created For Tree Data struct
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
    




#Begin implementation of Tree 
tree = Tree(20)
#Tree instance created
print(tree)
print(tree.val)
#Tree has been created and data has been properly stored inside


#Creating the actual tree struct
tree.left = Tree(18)
tree.right = Tree(22)
#Children nodes have been instantiated 
print(tree.left.val)
print(tree.right.val)
#Children Trees Complete 
#Insert Function ran
tree.insert(15)
#Insert function complete

#Insert function tested 
print(tree.left.left.val)






