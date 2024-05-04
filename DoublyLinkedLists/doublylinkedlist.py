class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        """
        adds a node in the last of DLL
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop(self):
        """
        returns the last node of DLL and remove it
        """
        if self.head is None:
            return None
        
        temp = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp
    
    def prepend(self, value):
        """
        adds a new node to the beginning of the DLL
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        return True
    
    def pop_first(self):
        """
        returns the first node from the DLL and removes it
        """
        if self.length == 0:
            return None
        
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1
        return temp
    
    def get(self, index):
        """
        returns the node at given index
        """
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp
    
    def set_value(self, index, value):
        """
        sets the value of the node at the given index
        """
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """
        inserts a new node at the given index
        """
        if index < 0 or index > self.length:
            return False
 
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            after = self.get(index)
            before = after.prev
            new_node.next = after
            new_node.prev = before
            after.prev = new_node
            before.next = new_node
            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_dll = DoublyLinkedList(7)
my_dll.append(10)
my_dll.append(15)
my_dll.append(20)
my_dll.print_list()
print("\n", my_dll.pop().value)
my_dll.print_list()
print("\n", my_dll.pop().value)
my_dll.print_list()
print("\n", my_dll.pop().value)
my_dll.print_list()
print("\n", my_dll.pop().value)
my_dll.print_list()
