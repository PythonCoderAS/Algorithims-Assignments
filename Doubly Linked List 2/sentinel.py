class DoubleNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = DoubleNode()
        self.tail = DoubleNode(prev=self.head)
        self.head.next = self.tail
        self.len = 0
    
    def __str__(self):
        """Fix me."""
        if self.head.next is None:
            return "[]"
        curr = self.head.next
        ans = "[{}".format(str(curr.data))
        curr = curr.next
        while curr != self.tail:
            ans += ", {}".format(curr.data)
            curr = curr.next
        return ans + "]"
    
    def __len__(self):
        return self.len
    
    def is_empty(self):
        return self.len == 0
    
    def insert_after(self, node, data):
        """Adds a new DoubleNode with data after node."""
        new_node = DoubleNode(data, node.next, node)
        node.next.prev = new_node
        node.next = new_node
        self.len += 1
        if self.tail.prev is None:
            self.tail.prev = new_node
        return new_node
    
    def remove_after(self, node):
        """Remove the DoubleNode after node."""
        return self.remove(node.next)
    
    def add_front(self, data):
        """Adds a Node with data at the head of the list."""
        return self.insert_after(self.head, data)
    
    def search(self, item):
        """Returns whether item is in the list."""
        return self.index(item)
    
    def add_back(self, data):
        """Adds a Node with data at the end of the list."""
        return self.insert_after(self.tail.prev, data)
    
    def index(self, data):
        """Returns the index of the DoubleNode with data in the list."""
        curr = self.head.next
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
        Fix me."""
        if pos == 0:
            return self.add_front(data)
        elif pos == self.len:
            return self.add_back(data)
        else:
            curr = self.head
            while pos > 0:
                curr = curr.next
                pos -= 1
            node = DoubleNode(data, curr, curr.prev)
            curr.prev.next = node
            curr.prev = node
            self.len += 1
            return node
    
    def remove(self, data):
        """Removes the Node with data from the list.
        Fix me."""
        return self.pop(self.index(data))
        
    
    def pop(self, pos):
        """Removes the Node at index pos from the list.
        Fix me."""
        if pos == -1:
            return None
        elif pos == 0:
            if self.len == 1:
                node = self.head
                self.head = self.tail = None
                self.len -= 1
                return node
            else:
                node = self.head
                self.head = self.head.next
                self.head.prev = None
                self.len -= 1
                return node
        elif pos == self.len - 1:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
            return node
        else:
            curr = self.head
            while pos > 0:
                curr = curr.next
                pos -= 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.len -= 1
            return curr



if __name__=="__main__":
    lst = DoublyLinkedList()
    lst.add_back(1)
    lst.add_back(2)
    lst.add_back(3)
    print(lst)
    print(lst.index(2))
    lst.insert(2, 9)
    print(lst)
    lst.remove(2)
    print(lst)
    lst.pop(1)
    print(lst)
