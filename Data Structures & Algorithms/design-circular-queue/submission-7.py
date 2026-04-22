class ListNode:
    def __init__(self,val = -1,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    

class MyCircularQueue:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.front = ListNode()
        self.rear = ListNode()
        self.front.prev = self.rear
        self.rear.next = self.front
        

    def enQueue(self, value: int) -> bool:
        
        if self.size == self.capacity:
            return False
        
        newNode = ListNode(value)

        self.rear.next.prev = newNode
        newNode.next = self.rear.next
        self.rear.next = newNode
        newNode.prev = self.rear

        self.size += 1
        return True

    def deQueue(self) -> bool:
        
        if self.size == 0:
            return False
        print(self.size)

        temp = self.front.prev
        temp.prev.next = self.front
        self.front.prev = temp.prev
        self.size -= 1

        return True

        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.front.prev.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.rear.next.val
        

    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()