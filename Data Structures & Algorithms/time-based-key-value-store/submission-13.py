from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.my_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_map[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        current_list = self.my_map[key]
        print(current_list,key)
        left = 0
        right = len(current_list) - 1
        res = ""
        while left <= right:
            middle = (left + right) // 2
            
            if current_list[middle][1] == timestamp:
                res = current_list[middle][0]
                break
            
            if current_list[middle][1] <= timestamp:
                res = current_list[middle][0]
                print(left,res)
                left = middle + 1
            else:
                right = middle - 1

        return res
        
