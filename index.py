class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def push_to_the_end(self, data):
        new_node = Node(data)
        current = self
        while current.next:
            current = current.next
        current.next = new_node

    def push_behind(self, node, data):
        new_node = Node(data)
        current = self
        while current:
            if current == node:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Uzel s hodnotou {node.data} nebyl nalezen.")

    def remove(self, data):
        current = self
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.data = current.next.data
                    self.next = current.next.next
                return
            prev = current
            current = current.next
        print(f"Uzel s hodnotou '{data}' nebyl nalezen.")

    def get_node(self, index):
        current = self
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        print(f"Uzel na pozici {index} neexistuje.")
        return None

    def len(self):
        current = self
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def get_first(self):
        return self

    def get_last(self):
        current = self
        while current.next:
            current = current.next
        return current

    def print_list(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    head = Node(10)
    head.push_to_the_end(20)
    head.push_to_the_end(30)
    head.push_to_the_end(40)

    head.print_list()

    node = head.get_node(1)
    if node:
        head.push_behind(node, 25)

    head.print_list()

    head.remove(30)

    head.print_list()

    first_node = head.get_first()
    last_node = head.get_last()
    print({first_node.data})
    print({last_node.data})

    print({head.len()})
