from collections import deque


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.storage.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.storage.popleft()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.storage) == 0
