"""
Name: Huixin Wang
Date: 
Description:
"""

# import the Stack class here
class Stack:
    def __init__(self):
        self.the_stack = []
        self.count = 0
        self.top = -1

    def __len__(self):
        return self.count

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self.the_stack.append(item)
        self.top += 1
        self.count += 1

    def pop(self):
        assert not self.is_empty(), "Empty stack"
        
        item = self.the_stack[self.top]
        self.top -= 1
        self.count -= 1
        del self.the_stack[len(self)]
        return item

    def peek(self):
        assert not self.is_empty(), "Empty stack"
        item = self.the_stack[self.top]
        return item

def check_for_balanced_parenthesis(string_of_parenthesis):
    # Your solution goes here 
    parenthesis_stack = Stack()
    balanced = True

    for i in range(len(string_of_parenthesis)):
        current_parenthesis = string_of_parenthesis[i]
        if current_parenthesis == "(":
            parenthesis_stack.push(current_parenthesis)
        else:
            if not parenthesis_stack.is_empty():
                parenthesis_stack.pop
            else:
                balanced = False
                break

    if balanced and parenthesis_stack.is_empty():
        return True
    else:
        return False

print(check_for_balanced_parenthesis("a(bc)d"))


