# print("Hello World")

# stack = []
# stack.append('A')
# stack.append('B')
# stack.append('C')

# print("This is the stack: ", stack)

class CustomNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# implement a stack
class CustomList:
    def __init__(self):
        self.head = None

    # push to beginning
    def push(self, data):
        new_node = CustomNode(data)
        # Case 1 - List is empty
        if self.is_empty():
            self.head = new_node
        # Case 2 - List is not empty
        else:
            new_node.next = self.head
            self.head = new_node

    # pop
    def pop(self):
        # Case 1 - List is empty
        if self.is_empty():
            return None
        # Case 2 - List is not empty
        else:
            popped_node = self.head
            self.head = self.head.next
            return popped_node.data

    # peek at top node in stack
    def peek(self):
        peek_node = self.head
        return peek_node.data

    # count
    def count(self):
        num_items = 0
        temp_head = self.head
        while temp_head is not None:
            num_items += 1
            temp_head = temp_head.next
        return num_items

    # isEmpty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # print list
    def print_list(self):
        temp_head = self.head
        if self.is_empty():
            print("The list is empty.\n")
        else:
            print("The data in the list is: ")
            while temp_head is not None:
                print(temp_head.data, end=" \n")
                temp_head = temp_head.next


print("New Stack Object:")
test_stack = CustomList()

print("Pushing new variables to the stack:")
test_stack.push("a")
test_stack.push(1)
test_stack.push("UwU")

print("Variable count:", test_stack.count())

print("Printing the variables in the list:")
test_stack.print_list()

print("Remove the first variable in the list:", test_stack.pop())

print("Look at the first variable in the stack: ", test_stack.peek())

print("Is the stack empty: ", test_stack.is_empty())

test_stack.print_list()
