

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, data):
        end = Node(data)
        node = self

        while node.next:
            node = node.next

        node.next = end


def delete_node(head, data):
    node = head
    if node.data == data:
        return head.next

    while node.next:
        if node.next.data == data:
            node.next = node.next.next
            return head
        node = node.next
    return head


def main():
    numbers = range(10)
    head = Node(-1)

    for n in numbers:
        head.append_to_tail(n)

    delete_node(head, 3)

    node = head
    while node:
        print(node.data)
        node = node.next

    print 'Done'

if __name__ == '__main__':
    main()
