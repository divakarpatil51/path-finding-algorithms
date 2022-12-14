from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]