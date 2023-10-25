#!/usr/bin/python3
"""Define module."""


class Node:
    """
    Node class
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance

        Args:
            data (int): The data value of the node
            next_node (Node): The reference to the next node (default is None)

        Raises:
            TypeError: If the data is not an integer
            TypeError: If the next_node is not None or a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data value of the node

        Returns:
            int: The data value of the node
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node

        Args:
            value (int): The data value of the node

        Raises:
            TypeError: If the data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node

        Returns:
            Node: The reference to the next node
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node

        Args:
            value (Node): The reference to the next node

        Raises:
            TypeError: If the next_node is not None or a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order)

        Args:
            value (int): The value of the new node
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list

        Returns:
            str: The string representation of the linked list
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
