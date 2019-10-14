from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because it's more efficient than a list since all items pulled will be from the front.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.len() == 0:
            return None
        else:
            return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
