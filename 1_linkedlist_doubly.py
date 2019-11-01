
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        node = self.tail
        node.next = DoubleNode(value)
        node.next.previous = node
        self.tail = node.next
        return


# Test your class here
linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node_tc = linked_list.head
while node_tc:
    print(node_tc.value)
    node_tc = node_tc.next

print("\nGoing backward through the list, should print 4, -2, 1")
node_tc = linked_list.tail
while node_tc:
    print(node_tc.value)
    node_tc = node_tc.previous





