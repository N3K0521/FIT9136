"""
Name: FIT9136 - Teaching Team
Date: 6 April 2022
Description: This python script define a function to read a string of parentheses from left to right and check whether the parentheses are balanced or not.
"""

# import the Stack class here
class Stack:

    # creates a new stack
    def __init__(self):
        self.the_stack = [] # represent the stack as a list
        self.count = 0 # indicate the current size of the stack
        self.top = -1 # indicate the top position of the stack
        
    # returns the number of items in the stack
    def __len__(self):
        return self.count
        
    # returns True if the stack is empty or False otherwise
    def is_empty(self):
        return len(self) == 0
        
    # pushes an item onto the top of the stack
    def push(self, item):
        self.the_stack.append(item)
        self.top += 1
        self.count += 1
        
    # removes and returns the top item on the stack
    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        
        item = self.the_stack[self.top]
        self.top -= 1
        self.count -= 1
        del self.the_stack[len(self)]
        return item
        
    # returns the item on the stack without removing it
    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        item = self.the_stack[self.top]
        return item

def check_for_balanced_parenthesis(string_of_parenthesis):
    # create a new stack
    parenthesis_stack = Stack()
    balanced = True
    
    # for each parenthesis encountered:
    for i in range(len(string_of_parenthesis)):
        current_parenthesis = string_of_parenthesis[i]
        # if it is an opening parenthesis:
        if current_parenthesis == "(":
            # “push” it onto the stack
            parenthesis_stack.push(current_parenthesis)
        # if it is a closing parenthesis 
        else:
            # and the stack is not empty:
            if not parenthesis_stack.is_empty():
                 # “pop” an opening parenthesis from the stack and continue processing
                parenthesis_stack.pop()              
            else:
                # but the stack is empty:
                balanced = False
                # stop processing (i.e. no matching opening parenthesis)
                break

    # at the end of processing:
    # if the stack is empty and all the parentheses were processed:
    # we have all matching pairs of parentheses
    if balanced and parenthesis_stack.is_empty():
        return True
    else:
        return False

print(check_for_balanced_parenthesis("a(bc)d)"))
