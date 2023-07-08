from linked_list import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList()

    # insert operation
    linked_list.insert_at_begining(20)
    linked_list.insert_at_begining(10)
    linked_list.insert_at_begining(23)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(8)
    linked_list.insert_at(44,30)
    linked_list.insert_at(14,8)
    linked_list.print()

    # delete operation
    linked_list.delete_at_end()
    linked_list.delete_at_begining()
    linked_list.delete_at(44)
    linked_list.print()