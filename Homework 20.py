


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self):
        if not self.head:
            return None
        elif not self.head.next:
            removed_value = self.head.value
            self.head = None
            return removed_value
        else:
            current = self.head
            while current.next.next:
                current = current.next
            removed_value = current.next.value
            current.next = None
            return removed_value


my_list = LinkedList()


my_list.append(1)
my_list.append(2)
my_list.append(3)

#
removed_value = my_list.remove()
print("Removed value:", removed_value)  



# ----------------------------------------------------------------------------------------





class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

my_stack = Stack()


my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)


popped_value = my_stack.pop()
print("Popped value:", popped_value)  
