from PIL import Image

#
#Author: Aaron Thomas 
#Date  : 3/22/2022
#SYNOP : This is a file that will act as an introduction to a singly linked list 


#Node Class creation 
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
#LinkedList Class creation
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        #New Node created
        new_node = Node(data)
        #associate new node with linked list
        new_node.next = self.head
        self.head = new_node


    
    def printNodes(self):
        temp = self.head
        while(temp):
            print(temp.data.show())
            temp = temp.next
    
    def getLength(self):
        count = 0
        current = self.head
        while(current):
            count = count + 1
            current = current.next
        return count
    

    

        
            


#Image Collection
im1 = Image.open("IMG_0827.JPG")
im2 = Image.open("IMG_0927.JPG")
im3 = Image.open("All-Male-Animal-Male-Monochrome-Nara-Shikamaru-Naruto-.jpg")
im4 = Image.open("anime-one-piece-brook-one-piece-franky-one-piece-wallpaper-preview.jpg")
#im1.show()
#im2.show()

    


#Building the linked list
ll = LinkedList()
ll.insert(im1)
ll.insert(im2)
ll.insert(im3)
ll.insert(im4)




#How many nodes are in the Linked List
print(ll.getLength())
#Display the pictures stored in the linked list
ll.printNodes()















    
    


