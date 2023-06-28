#!/usr/bin/python3
"""Node module"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initialize Node instance with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """Initialize SinglyLinkedList instance"""
        self.head = None

    def __str__(self):
        """Convert the list to a string"""
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
