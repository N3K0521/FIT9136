"""
Name: FIT9136 - Teaching Team
Date: 6 April 2022
Description: 
"""
# import the Queue class here
class Queue:
    '''implementation of the Queue ADT using an array structure with bounded capacity'''

    # creates a new queue
    def __init__(self, size):
        self.the_queue = [0] * size # represent a queue with fixed size
        self.count = 0
        self.front = 0
        self.rear = len(self.the_queue) - 1
        
    # returns the number of items in the queue
    def __len__(self):
        return self.count
        
    # returns True if the queue is empty or False otherwise
    def is_empty(self):
        return len(self) == 0
        
    # returns True if the queue is full or False otherwise
    def is_full(self):
        return len(self) == len(self.the_queue)
        
    # appends the given item to the end of a circular queue
    def append(self, item):
        assert not self.is_full(), "Cannot append to a full queue"
        self.rear = (self.rear + 1) % len(self.the_queue)
        self.the_queue[self.rear] = item
        self.count += 1
        
    # removes and returns the first item of a circular queue
    def serve(self):
        assert not self.is_empty(), "Cannot serve an empty queue"
        
        item = self.the_queue[self.front]
        self.front = (self.front + 1) % len(self.the_queue)
        self.count -= 1
        
        return item

class Master:
    def __init__(self):
        self.job_queue = Queue(5)
        
    def enter(self, agent_id):
        self.job_queue.append(agent_id)
    
    def exit(self):
        print("This agent has left the critical region: ", self.job_queue.serve())
