class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def r_insert(self, root, value):
        if root == None:
            return Node(value)
        if value < root.value:
            root.left = self.r_insert(root.left, value)
        if value > root.value:
            root.right = self.r_insert(root.right, value)
        return root
    
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def r_contains(self, root, value):
        if root == None:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return self.r_contains(root.left, value)
        if value > root.value:
            return self.r_contains(root.right, value)
    
    def r_delete(self, root, value):
        if root == None:
            return None
        if value < root.value:
            root.left = self.r_delete(root.left, value)
        elif value > root.value:
            root.right = self.r_delete(root.right, value)
        else:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                sub_tree_min = self.min_value(root.right)
                root.value = sub_tree_min
                root.right = self.r_delete(root.right, sub_tree_min)
        return root
    
    def min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.value


my_bst = BinarySearchTree()
root = my_bst.r_insert(my_bst.root, 47)
my_bst.r_insert(root, 21)
my_bst.r_insert(root, 97)
my_bst.r_insert(root, 14)
my_bst.r_insert(root, 24)
my_bst.r_insert(root, 84)
my_bst.r_insert(root, 22)
my_bst.r_insert(root, 26)


print(my_bst.r_contains(root, 21))

my_bst.r_delete(root, 21)

print(my_bst.r_contains(root, 21))