class myList:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = myList(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def sort_list(self):
        if self.head is None:
            return

        new_head = None
        current = self.head

        while current:
            next_node = current.next
            if new_head is None or current.data <= new_head.data:
                current.next = new_head
                new_head = current
            else:
                search = new_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node

        self.head = new_head

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += str(current.data) + ' '
            current = current.next
        return res


listt = LinkedList()
listt.append(5)
listt.append(2)
listt.append(3)
listt.append(4)
listt.append(1)
print(f"До сортировки: {listt}")
listt.sort_list()
print(f"После сортировки: {listt}")
