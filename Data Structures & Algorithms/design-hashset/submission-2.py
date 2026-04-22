class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        index = key % (10**4)
        node = self.set[index]
        while node.next:
            if node.next.key == key:
                return
            node = node.next
        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % (10**4)
        node = self.set[index]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next        

    def contains(self, key: int) -> bool:
        index = key % (10**4)
        node = self.set[index]
        while node.next:
            if node.next.key == key:
                return True
            node = node.next
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)