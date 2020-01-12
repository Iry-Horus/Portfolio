class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
            
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, tree):
        self.left = tree

    def set_right(self, tree):
        self.right = tree

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def create_string(self, spaces): 
        info = ' ' * spaces + str(self.data) 
        if self.left != None: 
            info += '\n(l)' + self.left.create_string(spaces+4) 
        if not self.right == None: 
            info += '\n(r)' + self.right.create_string(spaces+4) 
        return info       

    def __str__(self): 
        representation = self.create_string(0) 
        return representation  
