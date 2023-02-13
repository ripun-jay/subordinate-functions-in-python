class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next  
        print(llstr)
 
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_list_values(self, datas):
        for data in datas:
            self.insert_at_end(data)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count
    
    def remove_at_index(self, index):
        if index == 0:
            self.head = self.head.next

        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count+=1
            itr = itr.next

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)

        count = 0        
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            count+=1
            itr = itr.next

    def remove_the_value(self, data):
        itr = self.head

        if itr is None:
            raise Exception("Remove Operation on Empty Linked List is not Valid")
        
        while itr:
            if itr.data == data:
                itr.data = itr.next.data
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(4)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_list_values([8,9])

    ll.insert_at_index(3,7)
    ll.remove_at_index(3)
    ll.remove_the_value(7)
    ll.remove_the_value(5)

    
    
    print(ll.length())
    ll.print() 