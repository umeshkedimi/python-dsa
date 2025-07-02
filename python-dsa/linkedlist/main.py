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

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

my_linked_list = LinkedList(5)
my_linked_list.append(10)
my_linked_list.append(15)

# print(my_linked_list.tail.next)
my_linked_list.print_list()