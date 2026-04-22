from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.my_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_map[key].append((timestamp,value))
        
    
    def get(self, key: str, timestamp: int) -> str:
        curr_list = self.my_map[key]
        low, high = 0, len(curr_list) - 1
        res = ""
        
        while low <= high:
            mid = low + (high - low) // 2
            time, val = curr_list[mid]
            
            if time == timestamp:
                return val
            elif time < timestamp:
                res = val  
                low = mid + 1
            else:
                high = mid - 1

        return res

        return  value if time <= timestamp else ""