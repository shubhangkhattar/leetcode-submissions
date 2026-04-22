class ListNode:
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None



class MyHashMap:

    def __init__(self):
        self.my_map = [ListNode(0,0) for i in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        index = key % (10**4)
        node = self.my_map[index]
        while node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = ListNode(key,value)
        

    def get(self, key: int) -> int:
        index = key % (10**4)
        node = self.my_map[index]
        while node.next:
            if node.next.key == key:
                return node.next.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = key % (10**4)
        node = self.my_map[index]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)