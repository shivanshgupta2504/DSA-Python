class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    
    def r_insert(self, root, value):
        if root == None:
            return Node(value)
        if value < root.value:
            root.left = self.r_insert(root.left, value)
        if value > root.value:
            root.right = self.r_insert(root.right, value)
        return root
    
    
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
    
    def bfs(self, root):
        current_node = root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return result
    
    def dfs_pre_order(self, root):
        result = []
        if root is None:
            return result
        result.append(root.value)
        if root.left is not None:
            result.extend(self.dfs_pre_order(root.left))
        if root.right is not None:
            result.extend(self.dfs_pre_order(root.right))
        
        return result
    
    def dfs_post_order(self, root):
        result = []
        if root is None:
            return result
        if root.left is not None:
            result.extend(self.dfs_post_order(root.left))
        if root.right is not None:
            result.extend(self.dfs_post_order(root.right))
        result.append(root.value)

        return result
    
    def dfs_in_order(self, root):
        result = []
        def traverse(root):
            if root.left is not None:
                traverse(root.left)
            result.append(root.value)
            if root.right is not None:
                traverse(root.right)
        
        traverse(root)
        return result
        

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
print(my_bst.bfs(root))
print(my_bst.dfs_pre_order(root))
print(my_bst.dfs_post_order(root))
print(my_bst.dfs_in_order(root))
