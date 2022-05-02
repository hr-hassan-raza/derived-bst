import bst
from queue import Queue
class Derived_BST(bst.BST):
    def __init__(self):
        super().__init__() #A super constructor called from child class

    def get_node_pointer(self, node, value):
        """ 
        Function to get the node pointer
        This function returns node with given value
        The argument of functions are node and value

        """
        if node is None:
            return 
        if node.value==value:
            return node
        
        temp = self.get_node_pointer(node.left, value)
        if temp:
            return temp
        temp = self.get_node_pointer(node.right, value)
        if temp:
            return temp

    def is_leaf(self, node): #Function to check if the node given is leaf
        """
        This function checks if the node passed as parameter is leaf
        node in tree

        """
        node = self.get_node_pointer(self.get_root(), node.value) ## Getting node value
        if (node == None):       
            return False
        if node.left == None and node.right == None: #If both left nd right are None, then it is leaf
            return True
        else:
            return False
       
    def is_branch(self, node): #Function to check if the node given is branch
        """
        This function checks if the node passed as parameter is branch
        node in tree
        
        """
        node = self.get_node_pointer(self.get_root(), node.value) ##Getting node value
        if (node==None):
            return False
        if node.left is not None or node.right is not None: #If any one of the right or left is None, then it is branch
            return True
        else:
            return False

    def parent_node(self, value):#Function to find parent of node with given value
        """
        Function to find parent node of given value in tree
        """
        temp = self.get_root() # Getting root node
        parent = None #initializing the parent value
        if(temp == None):
            return None
        while(temp != None):
            if(value < temp.value): ## Going towards left in tree
                parent = temp.value
                temp = temp.left
            elif (value > temp.value): ## Going towards right in tree
                parent = temp.value
                temp = temp.right
            else:
                break
        return parent

    def total_leaf_nodes(self, node): #Finds the total number of leaf nodes in the BST
        """
        The function counts the total number of leaf nodes in the BST through recursive
        approach
        
        """
        if node is None: #If BST empty
            return 0
        if node.left is None and node.right is None: #If only one element in the BST
            return 1
        else:
            return self.total_leaf_nodes(node.left) + self.total_leaf_nodes(node.right)
    
    def total_leaf_nodes_iterative(self): #
        """
        Finds the total number of leaf nodes in the BST iteratively
        """
        temp = self.get_root()
        if not temp: #If BST empty
            return 0
        que = Queue() #inititalizing a queue
        count = 0 #Initializing number of leaves
        que.put(temp)
        while(not que.empty()):
            node = que.queue[0]
            que.get()

            if node.left is not None:
                que.put(node.left)
            if node.right is not None:
                que.put(node.left)
            if node.left is None and node.right is None:
                count+=1
        return count

    def total_nonleaf_nodes(self):
        """
        This function finds total number of nonleaf nodes in the BST

        """
        leafnodes = self.total_leaf_nodes(self.get_root())
        return self.size-leafnodes
    
    def get_max(self):
        """
        Finds the value of the maximum node in the BST

        """
        temp = self.get_root()
        while(temp.right): #Traversing to the extreme right
            temp = temp.right
        return temp.value
    
    def get_min(self):
        """
        Finds the value of the minimum node in the BST

        """
        temp = self.get_root()
        while(temp.left): #Traversing to the extreme left
            temp = temp.left
        return temp.value

    def breadth_first(self):
        """
        breadth first search of tree
        """
        temp = self.get_root() ## getting root node
        queue = [temp] ## making queue and inserting root node
        while queue: ## iterating through queue
            temp_list = list()
            for n in queue:
                print (n.value,' ', end=''),
                if n.left: temp_list.append(n.left) # Traversing to the extreme left
                if n.right: temp_list.append(n.right) # Traversing to the extreme right
            print(" ")
            queue = temp_list
