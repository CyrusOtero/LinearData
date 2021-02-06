# Cyrus Otero
# 2/5/2021
# SNEK

# Same as single except assigns default value to previous pointer
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinks:
    def __init__ (self):
        self.head = None
    
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

    def append_left(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev =  None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            current.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    
    def display(self):
        listofData = []
        current = self.head
        
        while current.next!=None:
            listofData.append(current.data) 
            current = current.next   
        listofData.append(current.data)          
        print(listofData)

    # this is much simpler than my previous version
    # assigns previous to None and head to current
    def pop(self):
        current = self.head
        current = current.next
        current.prev = None
        self.head = current

    def pop_right(self):
        current = self.head
        while current.next.next != None:
            current = current.next
        current.next = None

    def contains(self, data):
        current = self.head
        current_index = 0
        try:
            while True:
                if current.data == data:
                    print(f'The list contains {data}')
                    return
                current_index+=1
                current = current.next
        except:
            print(f'The list does not contain {data}')

twolinks = DoubleLinks()

twolinks.append(1)
twolinks.append(2)
twolinks.append(3)
twolinks.append(4)
twolinks.append_left(6)

twolinks.display()

twolinks.pop()
twolinks.pop_right()

twolinks.display()

twolinks.contains(2)