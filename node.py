class Node:
    def __init__(self, key, parent):
        self.data = key
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return self.data
