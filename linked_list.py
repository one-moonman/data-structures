class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return "{} -> {}".format(self.data, self.next)

# basic Linked-list that could be used as queue or stack too.


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # pushes node to the front
    def push(self, data: any) -> any:
        node = Node(data)
        node.next = self.head
        self.head = node
        return node

    # pops node from the back
    def pop(self) -> any:
        node = self.head
        if node.next is None and node is not None:
            self.head = None
            return

        while node.next.next is not None:
            node = node.next
        node.next = None
        return

    # appends node from the back
    def append(self, data: any) -> any:
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        return node

    # removes node from the front
    def remove(self) -> any:
        node = self.head
        if node.next is None and node is not None:
            self.head = None
            return

        node = self.head.next
        self.head = node
        return

    def first(self) -> any:
        return self.head.data

    def last(self) -> any:
        node = self.head
        while node.next is not None:
            node = node.next
        return node.data

    def at(self, index: int) -> any:
        node = self.head
        i = 0
        while i is not index:
            node = node.next
            i += 1
        return node.data


ll = LinkedList()
ll.push(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)

print(ll)
