# Binary Search Tree Implementation
#
# 
#
#

# Main class for BST
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # BST search method()
    def search(self, desired_key):
        if self.root is None:
            self.root = desired_key
            return desired_key

        current_node = self.root
        while current_node is not None:
            # return the node if the key matches
            if current_node == desired_key:
                return current_node

            # Navigate to the left if the search key
            # is less than the node's key
            elif desired_key < current_node.key:
                current_node = current_node.left


            # Navigate to the right if the search key
            # is greater than the node's key
            else:
                current_node = current_node.right
                
        # The key was not found in the tree
        return None
        
    # BST insert method
    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the 
                    # left child
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None 
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the 
                    # right child
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

# Node class for BST 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None




# Driver code for testing insert and search
tree = BinarySearchTree()
node_a = Node(17)
node_b = Node(32)
node_c = Node(10)
node_d = Node(3)
node_e = Node(21)

tree.insert(node_a)
tree.insert(node_b)
tree.insert(node_c)
tree.insert(node_d)
tree.insert(node_e)

# Search for key
key_one = 3
found_node = tree.search(key_one)
print(found_node)
if found_node is not None:
    print('Found node with key = %d' % found_node.key)
else:
    print('Key', key_one, 'not found.')

# Searh for another key
key_two = 99
found_node = tree.search(key_two)
if found_node is not None:
    print('Found node with key = %d' % found_key.key)
else:
    print('Key', key_two, 'not found.')

