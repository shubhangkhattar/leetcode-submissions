class MyHashSet:

    def __init__(self):
        self.my_list = []
        

    def add(self, key: int) -> None:
        if key not in self.my_list:
            self.my_list.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.my_list:
            self.my_list.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.my_list
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)