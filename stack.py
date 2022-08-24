class Stack:

    def __init__(self):
        self._stack = []

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return not self._stack

    def size(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

