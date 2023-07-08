from node import Node

class LinkedList:
    """Linked list class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def insert_at_begining(self, data):
        """Insert new node at the begining"""
        new_node = Node(data,None,None)
        if self.head is None:
            self.head=self.tail=new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert new node at the end"""
        new_node = Node(data,None,None)
        if self.head is None:
            self.head=self.tail=new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at(self, data, position):
        """Insert new node to the given position"""
        if position < 0:
            print("Invaid position")
            return
        elif position == 0:
            self.insert_at_begining(data)
            return
        elif position == self.length()-1:
            self.insert_at_end(data)
            return
        else:
            temp = self.head
            i = 0

            while i < position:
                temp = temp.next
                i += 1

            new_node = Node(data, None, None)
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node
            new_node.next.prev = new_node

    def delete_at_begining(self):
        """Delete first node"""
        if self.head is None:
            print("Linked list is empty")
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        """Delete last node"""
        if self.tail is None:
            print("Linked list is empty")
            return

        self.tail.prev.next = None
        self.tail = self.tail.prev

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