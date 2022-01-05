#!/usr/bin/env python

"""
Queue: FIFO
Build circle version of queue
"""


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.rear = 0
        self.front = 0
        self.size = size

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is full.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

