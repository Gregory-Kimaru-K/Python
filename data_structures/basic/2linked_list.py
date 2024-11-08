class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}"
    

class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None