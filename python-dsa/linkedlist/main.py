class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

my_linked_list = LinkedList(5)

print(my_linked_list.head.value)