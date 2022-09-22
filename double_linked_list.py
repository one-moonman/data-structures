class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return " {} -> {}".format(self.data, self.next)

# basic Linked-list that could be used as queue or stack too.


class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None

    def append(self, data: any) -> any:
        node = Node(data)
        if self.head is None:
            self.head = node
            return node

        current = self.head
        while current.next:
            current = current.next

        node.next = self.head
        node.prev = current

        self.head.prev = node
        current.next = node
        return node

    def __repr__(self):
        node = self.head
        nodes = []
        nodes.append(str(node.data))
        node = node.next
        while node is not self.head:
            nodes.append(str(node.data))
            node = node.next
        nodes.insert(0, "<-")
        nodes.append("->")
        return " <-> ".join(nodes)


dd = DoubleLinkedList()
dd.append("1")
dd.append("2")
print(dd)
