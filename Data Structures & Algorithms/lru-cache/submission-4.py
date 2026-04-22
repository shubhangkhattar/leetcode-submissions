class Node:

    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.front = Node() 
        self.rear = Node()
        self.front.next = self.rear
        self.rear.prev = self.front

    def _add_to_front(self,node):
        node.next = self.front.next
        node.prev = self.front
        node.next.prev = node
        self.front.next = node        

    def _del_node(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self._del_node(node)
        self._add_to_front(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._del_node(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
        
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            node = self.rear.prev
            del self.cache[node.key]
            self._del_node(node)
        
