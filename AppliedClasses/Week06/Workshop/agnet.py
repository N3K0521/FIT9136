"""
Name: Huixin Wang
Date: 
Description: 
"""

# import the Queue class here
class Queue:
    def __init__(self, size):
        self.the_queue = [0] * size
        self.count = 0
        self.front = 0
        self.rear = len(self.the_queue) - 1

    def __len__(self):
        return self.count
    
    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) == len(self.the_queue)

    def append(self, item):
        assert not self.is_full, "The queue is full"
        self.rear = (self.rear + 1) % len(self.the_queue)
        self.the_queue[self.rear] = item
        self.count += 1

    def serve(self):
        assert not self.is_empty, "The queue is empty"
        item = self.the_queue[self.front]
        self.front = (self, front+1) % len(self.the_queue)
        self.count -= 1

        return item

class Master:
    # Your solution goes here
    def __init__(self):
        self.job = Queue(5)

    def enter(self, agent_id):
        self.job.append(agent_id)

    def exit(self):
        print("Agent left.", self.job.serve())
        
