#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
      """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get/set the next node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Represent a singly-linked list."""
    
    def __init__(self)
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList."""
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            tmp = Node(value, self.__head)
            self.__head = tmp

    def __str__(self):
        return "{:d}".format(self.__head.data)
