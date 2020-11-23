# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# ERIN OCONNELL

class NaivePriorityQueue:

    def __init__(self):
        self.data = []

    def enqueue(self,appendee):
        self.data.append(appendee)    

    def dequeue(self):
       return self.data.pop()