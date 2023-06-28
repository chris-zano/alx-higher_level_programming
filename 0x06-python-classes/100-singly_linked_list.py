#!/usr/bin/python3
"""
100-singly_linked_list.py
"""


class Node:
    """
    node structure for a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        initializes the node object
        Args:
            data: the data attribute of the node object
            next_node: node object of the next node in the list
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node Object")

        self.__data = data
        self.__next_node = next_node

        return

    @property
    def data(self):
        """
        getter for the data attribute of the Node Object
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        setter for the data attribute of the Node Object
        Args:
            value: new data attribute value
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value
        return

    @property
    def next_node(self):
        """
        getter for next_node attribute of Node object
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for next_node attribute of the Node object
        Args:
            value (Node): new value for next_node attribute
        """

        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node Object")

        self.__next_node = value
        return


class SinglyLinkedList:
    """
    defines a singly linked list
    Attributes:
        __head (Node): head of the linked list
    """

    def __init__(self):
        """
        simple initialization of the linked list
        """

        self.__head = None
        return

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
            in the list(increasing order)
        Args:
         value (int): data stored inside the new node

        Returns:
            None
        """

        new_node = Node(value)
        temp = self.__head
        if temp is None or temp.data >= value:
            if temp:
                new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data >= value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    def __str__(self):
        """
        a readable representation of the linked list
        """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
