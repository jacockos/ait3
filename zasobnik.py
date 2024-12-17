class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):

        self.stack.append(item)

    def pop(self):

        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Zásobník je prázdný.")
            return None

    def is_empty(self):

        return len(self.stack) == 0

    def print_all(self):

        if self.is_empty():
            print("Zásobník je prázdný.")
        else:
            print("Prvky v zásobníku:", self.stack)


if __name__ == "__main__":

    stack = Stack()


    stack.push(1)
    stack.push(2)
    stack.push(3)


    stack.print_all()


    print("Odebraný prvek:", stack.pop())


    stack.print_all()
