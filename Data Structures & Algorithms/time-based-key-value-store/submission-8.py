class TimeMap:

    def __init__(self):
        self.my_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
         self.my_map[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.my_map[key]) - 1
        ans_value = ""
        while left <= right:
            mid = left + (right-left) // 2
            value, mid_time = self.my_map[key][mid]
            if mid_time == timestamp:
                return value
            
            if mid_time < timestamp:
                left = mid + 1
                ans_value = value
            else: 
                right = mid - 1

        return ans_value
