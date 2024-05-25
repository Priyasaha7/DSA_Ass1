class Node:
    def _init_(self, data, next = None):
        self.data = data
        self.next = next

class SLL:
    def _init_(self, ):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.size() == 0
    
    def _str_(self):
        l = []
        trav = self.__head
        while trav is not None:
            l.append(trav.data)
            trav = trav.next
        
        return '<->'.join(map(str,l))
    
    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
        else:
            trav = self.__head
            while trav.next:
                trav = trav.next
            trav.next = newNode
        self.__size += 1

    def prepend(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
        else:
            newNode.next = self.__head
            self.__head = newNode
        self.__size += 1

    def insertAt(self, index, data):
        if index < 0 or index > self.size():
            raise Exception("Invalid index")
        if index == 0:
            self.prepend(data)
        elif index == self.size():
            self.append(data)
        else:
            id = 0
            trav = self.__head
            while id !=index-1:
                id += 1
                trav = trav.next
            newNode = Node(data, trav.next)
            newNode.next = trav.next
            trav.next = newNode
            self.__size += 1

    def deleteAt(self, index):
        if index < 0 or index > self.size():
            raise Exception("Invalid index")
        else:
            id = 0
            trav = self.__head
            while id != index-1:
                id += 1
                trav = trav.next
            temp = trav.next
            trav.next = trav.next.next
            del temp
            self.__size -= 1

    def reverse(self):
        prev = None
        curr = self.__head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.__head = prev

    def rotateRight(self, k):
        if self.__head == None or k == 0:
            return
        length = self.size()
        k %= length
        if k == 0:
            return
        prev = None
        curr = self.__head
        for i in range(length - k):
            prev = curr
            curr = curr.next
        new_head = curr
        while curr.next:
            curr = curr.next
        curr.next = self.head
        self.head = new_head
        prev.next = None

    def middle(self):
        if self.__head == None:
            return None
        slow = self.__head
        fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def getIndex(self, data):
        index = 0
        trav = self.__head
        while trav:
            if trav.data == data:
                return index
            trav = trav.next
            index += 1
        return -1