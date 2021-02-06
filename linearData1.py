# Cyrus Otero
# 1/23/2021
# time to do some snake stuff

# I spent a long time trying to figure out how to append a node to the left of the list
# I never got it completely working, I put in some of my scrap code at the bottom so you can laugh at me
# Not even gonna look at where I left it :)

# Node class serves as template for all nodes, node will hold data and 'pointer' to next node
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_up:
    def __init__(self):
        self.head = node()

# CRAfTs a new node set at the end of the list
    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next!=None:
            current = current.next
        current.next = new_node

    def length(self):
        current=self.head
        total = 0
        while current.next!=None:
            total+=1
            current = current.next
        return total

    def display(self):
        elems = []
        current = self.head
        while current.next!=None:
            current = current.next
            elems.append(current.data)
        print(elems)

# gets data associated with specified index, kinda like dictionary, pretty koool
    def get(self, index):
        if index >= self.length():
            print('ERROR: Index out of range!')
            return None
        current_index = 0
        current=self.head
        while True:
            current = current.next
            if current_index==index: return current.data
            current_index+=1
# 'erases' node by changing the last node's pointer to the following node, uses specified index, preeeeetttttyyyy cooooooool
    def erase(self, index):
        if index>=self.length():
            print('ERROR: Index out of range!')
            return
        current_index = 0
        current=self.head
        while True:
            last_node = current
            current = current.next
            if current_index==index:
                last_node.next = current.next
                return
            current_index+=1 
# iterates along the linked list looking to match the inputted data with data associated with a node. if found: returns True, the data, and the index. else: returns False
    def contains(self, data):
        current = self.head
        current_index = 0
        try:
            while True:
                current = current.next
                if current.data==data: return True, current.data, current_index
                current_index+=1
        except:
            return False

# 'removes' the 1st node using the same method as the erase function
    def pop(self):
        current = self.head
        last_node = current
        current = current.next
        last_node.next = current.next
        return current.data        

    def pop_right(self):
        current = self.head
        while True:
            last_node = current
            current = current.next
            if current.next == None:
                last_node.next = current.next
                return current.data
                
list = linked_up()

print('beep boop.. makin\' the list')
list.append(1)
list.append(2)
list.append(3)
list.append(4)

# list.append_left(7)
# list.clearList()

print('displaying list')
list.display()

print(f'The list is {list.length()} nodes long')
print(f'Element at 2nd Index: {list.get(2)}')

list.erase(2)
print('Removed element at 2nd Index')

print(f'The list is now {list.length()} nodes long')
print(f'New Element at 2nd Index: {list.get(2)}')

print('displaying list')
list.display()

print('hmm lets see if this list has the number 4 in it')
print(list.contains(4))

print('how about 2?')
print(list.contains(2))

list.display()
print('I don\'t like that first node')
list.pop()
print('gone')
list.display()


# this is taking forever
    # def clearList(self):
    #     current = self.head          

    #     while current.next != None:
    #         last_node = current
    #         current = current.next
    #         print(current.data)
    #         last_node.next = current.next              
    
    # def append_left(self, data):
    #     data = []
        # while True:
        #     last_node = current
        #     current = current.next
        #     if current.next == None:
        #         last_node.next = current.next
        #         return current.data       
        # while current.next != None:
        #     last_node = current
        #     current = current.next
        #     print(current.data)
        #     data.append(current.data)
        #     last_node.next = current.next
            
    
            # if current.next == None:
            #     last_node.next = current.next
            #     return  
                
        # for data in data:
            
        # print(current.data)
        # while current.next!=None:
        #     Lol_no_way = current.next.data
        #     print(current.next.data)
        # current = current.next
        #     current.data = Lol_no_way

        # while current.next!=None:
        #     print('hhh')
        #     current.data = current.next.data
        #     current = current.next
