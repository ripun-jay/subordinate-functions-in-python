class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class L:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        while itr:
            datais =  itr.data
            print(datais)
            nextis = itr.next
            itr = itr.next
        
ll = L()
ll.insert(5)
ll.insert(10)
ll.print()