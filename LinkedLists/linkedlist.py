class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    

    def append(self, value):
        """
        Add node to last of the list
        """
        new_node = Node(value)
        if self.head is None:  # if list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    

    def pop(self):
        """
        deletes node from the last of the list
        """
        if self.length == 0: # for empty LL
            return None
        
        if self.length == 1: # LL having 1 element
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        # LL having more than 1 elements
        temp = self.head
        pre = None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp
    

    def prepend(self, value):
        """
        adds a node in front of the list
        """
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    

    def pop_first(self):
        """
        removes a node in front of the list
        """
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp
    

    def get_node(self, index):
        """
        returns the node at the given index
        (indices starts from zero)
        """
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    

    def set_node(self, index, value):
        """
        sets the value of the node at the given index
        (indices starts from zero)
        """
        temp = self.get_node(index)
        if temp:
            temp.value = value
            return True
        return False
    

    def insert(self, index, value):
        """
        inserts a new node with the given value at the given index
        (indices starts from zero)
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get_node(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    

    def remove(self, index):
        """
        removes the node at the given index
        (indices starts from zero)
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get_node(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

    def reverse(self):
        """
        reverses the linked list
        """
        temp = self.head
        self.head = self.tail
        self.tail = self.head
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

    def middle_node(self):
        """
        returns the middle node of the linked list
        """
        if self.head is None or self.head.next is None:
            return self.head
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    
    def print_list(self):
        """
        prints the whole list
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    

my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
my_linked_list.print_list()
node = my_linked_list.pop()
print(node.value)
print(my_linked_list.length)
node = my_linked_list.pop()
print(node)