from node import Node

class LinkedList:
    """Linked list class"""
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        """Insert new node at the begining"""
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        """Insert new node at the end"""
        if self.head is None:
            self.head = Node(data, self.head)

        temp = self.head

        while temp.next:
            temp = temp.next

        new_node = Node(data, None)
        temp.next = new_node

    def insert_at(self, data, target):
        """Insert new node after the given node"""
        if self.head is None:
            self.head = Node(data, self.head)

        temp = self.head

        while temp and temp.data != target:
            temp = temp.next

        temp.next = Node(data, temp.next)

    def delete_at_begining(self):
        """Delete first node"""
        if self.head is None:
            print("Linked list is empty")
            return

        self.head = self.head.next

    def delete_at_end(self):
        """Delete last node"""
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_at(self, target):
        """Delete given node"""
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while temp and temp.next.data != target:
            temp = temp.next

        temp.next = temp.next.next

    def print(self):
        """Print all the nodes"""
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next

        print()