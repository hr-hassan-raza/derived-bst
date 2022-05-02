class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, value):
        current = self.root # Start from the root

        while current != None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else: # element matches current.value
                return True # Element is found

        return False
    
    # Insert value into the binary search tree
    # Return True if the value is inserted successfully 
    def insert(self, value):
        if self.root == None:
            self.root = self.create_new_node(value) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if value < current.value:
                    parent = current
                    current = current.left
                elif value > current.value:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if value < parent.value:
                parent.left = self.create_new_node(value)
            else:
                parent.right = self.create_new_node(value)

        self.size += 1 # Increase tree size
        return True # Element inserted
    
    # Insert a node into the binary search tree
    # Return True if the node is inserted successfully 
    def insert_node(self, node):
        if self.root == None:
            self.root = node # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if node.value < current.value:
                    parent = current
                    current = current.left
                elif node.value > current.value:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Attach node to the parent node
            if node.value < parent.value:
                parent.left = node
            else:
                parent.right = node

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for value
    def create_new_node(self, value):
        return TreeNode(value)

    # Return the size of the tree
    def get_size(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        lst = []
        self.inorder_helper(self.root,lst)
        return str(lst)

    # Inorder traversal from a subtree 
    def inorder_helper(self, root,inorder_lst):
        
        if root != None:
            self.inorder_helper(root.left, inorder_lst)
            #print(root.value, end = ' ')
            inorder_lst.append(root.value)
            self.inorder_helper(root.right,inorder_lst)
       

    # Postorder traversal from the root 
    def postorder(self):
        lst = []
        self.postorder_helper(self.root,lst)
        return str(lst)

    # Postorder traversal from a subtree 
    def postorder_helper(self, root,postorder_lst):
        if root != None:
            self.postorder_helper(root.left,postorder_lst)
            self.postorder_helper(root.right,postorder_lst)
            #print(root.value, end = ' ')
            postorder_lst.append(root.value)

    # Preorder traversal from the root 
    def preorder(self):
        lst = []
        self.preorder_helper(self.root,lst)
        return str(lst)

    # Preorder traversal from a subtree 
    def preorder_helper(self, root,preorder_lst):
        if root != None:
            print(root.value, end = ' ')
            preorder_lst.append(root.value)
            self.preorder_helper(root.left,preorder_lst)
            self.preorder_helper(root.right,preorder_lst)

    # Returns a path from the root leading to the specified value
    def path(self, value):
        lst = []
        current = self.root # Start from the root

        while current != None:
            lst.append(current) # Add the node to the list
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                break

        return lst # Return a list of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, value):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value: 
                parent = current
                current = current.right
            else:
                break # Value is in the tree pointed by current

        if current == None:
            return False # Value is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if value < parent.value:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parent_right_most = current
            right_most = current.left

            while right_most.right != None:
                parent_right_most = right_most
                right_most = right_most.right # Keep going to the right

            # Replace the value in current by the value in rightMost
            current.value = right_most.value

            # Eliminate rightmost node
            if parent_right_most.right == right_most:
                parent_right_most.right = right_most.left
            else:
                # Special case: parent_right_most == current
                parent_right_most.left = right_most.left     

        self.size -= 1
        return True # Value deleted

    # Return true if the tree is empty
    def is_empty(self):
        return self.size == 0
        
    # Remove all values from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def get_root(self):
        return self.root

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None


