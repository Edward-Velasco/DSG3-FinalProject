class Node:
    def __init__(self, maxSize) -> None:
        self.body = []
        self.maxSize = maxSize

    def enqueue(self, item):
        if self.maxSize != len(self.body):
            self.body.append(item)
            return 0
        else:
            print('queue is full')
            return -1
        
    def dequeue(self):
        if (len(self.body)!=0):
            return self.body.pop(0)
            
        else:
            print('queue is empty')
            return -1
        
    def peek(self):
        if len(self.body)!=0:
            return self.body[0]
        else:
            print('Queue is empty')
            return 0

    def is_empty(self):
        if len(self.body)!=0:
            return False
        return True