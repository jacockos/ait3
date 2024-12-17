class PriorityQueue:
    def __init__(self):
        self.queue = []


    def push(self, number, priority):
        self.queue.append((priority, number))
        self.queue.sort()

    def pop(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0

priority = PriorityQueue()
priority.push(5, 2)
priority.push(10, 1)
priority.push(3, 3)

print(priority.pop())
print(priority.pop())
print(priority.pop())