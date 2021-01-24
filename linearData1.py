# Cyrus Otero
# 1/23/2021
# time to do some snake stuff

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
        current_node = self.head
        while current_node.next!=None:
            current_node=current_node.next
            elems.append(current_node.data)
        print(elems)

# gets data associated with specified index, kinda like dictionary, pretty koool
    def get(self, index):
        if index >= self.length():
            print('ERROR: Index out of range!')
            return None
        current_index = 0
        current_node=self.head
        while True:
            current_node = current_node.next
            if current_index==index: return current_node.data
            current_index+=1
# 'erases' node by changing the last node's pointer to the following node, uses specified index, preeeeetttttyyyy cooooooool
    def erase(self, index):
        if index>=self.length():
            print('ERROR: Index out of range!')
            return
        current_index = 0
        current_node=self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index==index:
                last_node.next = current_node.next
                return
            current_index+=1 
# iterates along the linked list looking to match the inputted data with data associated with a node. if found: returns True, the data, and the index. else: returns False
    def contains(self, data):
        current_node = self.head
        current_index = 0
        try:
            while True:
                current_node = current_node.next
                if current_node.data==data: return True, current_node.data, current_index
                current_index+=1
        except:
            return False

# 'removes' the 1st node using the same method as the erase function
    def pop(self):
        current_node = self.head
        last_node = current_node
        current_node = current_node.next
        last_node.next = current_node.next        

list = linked_up()

print('beep boop.. makin\' the list')
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

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
