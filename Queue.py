class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):

        self.queue.append(item)

    def pop(self):

        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Fronta je prázdná.")
            return None

    def is_empty(self):

        return len(self.queue) == 0

    def print_all(self):

        if self.is_empty():
            print("Fronta je prázdná.")
        else:
            print("Prvky ve frontě:", self.queue)


if __name__ == "__main__":

    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)


    queue.print_all()


    print("Odebraný prvek:", queue.pop())


    queue.print_all()
