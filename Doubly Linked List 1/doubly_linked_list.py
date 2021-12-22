class DoubleNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def __str__(self):
        if self.head is None:
            return "[]"
        curr = self.head
        ans = "[{}".format(str(curr.data))
        curr = curr.next
        while curr is not None:
            ans += ", {}".format(curr.data)
            curr = curr.next
        return ans + "]"
    
    def __len__(self):
        return self.len
    
    def add_front(self, data):
        """Adds a Node with data at the head of the list."""
        self.head = Node(data, self.head)
        if self.tail is None:
            self.tail = self.head
        return self.head
    
    def search(self, item):
        """Returns whether item is in the list."""
        curr = self.head
        while curr is not None:
            if curr.data == item:
                return True
            else:
                curr = curr.next
        return False
    
    def add_back(self, data):
        """Adds a Node with data at the end of the list.
        (Formerly append. Delete me when fixed for DLLs.)"""
        if self.head is None:
            self.head = self.tail = Node(data)
            return self.head
        else:
            self.tail = Node(data, None, self.tail)
            return self.tail
    
    def index(self, data):
        """Returns the index of the DoubleNode with data in the list."""
        if self.head is None:
            return -1
        curr = self.head
        idx = 0
        while curr is not None:
            if curr.data == data:
                return idx
            else:
                curr = curr.next
                idx += 1
        return -1

    def insert(self, pos, data):
        """Adds a Node with data at index pos in the list.
        (Delete me when fixed for DLLs.)"""
        if pos == 0:
            self.head = Node(data, self.head)
            return self.head
        curr = self.head
        while pos > 1:
            curr = curr.next
            pos -= 1
        curr.next = Node(data, curr.next)
        return curr.next
    
    def remove(self, data):
        """Removes the Node with data from the list.
        (Delete me when fixed for DLLs.)"""
        curr = self.head
        if curr.data == data:
            self.head = self.head.next
            return curr

        prev = self.head
        while curr is not None:
            if curr.data == data:
                prev.next = curr.next
                return curr
            else:
                prev = curr
                curr = curr.next
        return None
    
    def pop(self, pos):
        """Removes the Node at index pos from the list.
        (Delete me when fixed for DLLs.)"""
        curr = self.head
        if pos == 0:
            self.head = self.head.next
            return curr
        
        while pos > 1:
            curr = curr.next
            pos -= 1
        
        node = curr.next
        curr.next = node.next
        return node


if __name__=="__main__":
    lst = DoublyLinkedList()
    #lst.append(1)
    #lst.append(2)
    #lst.append(3)
    print(lst)
    #print(lst.index(2))
    #lst.insert(2, 9)
    print(lst)
    #lst.remove(2)
    print(lst)
    #lst.pop(1)
    print(lst)
