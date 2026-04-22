class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        current_list = self.hashmap[key]
        if not current_list:
            return ""

        l = 0
        r = len(current_list) - 1
        result = ""
        while l <= r:
            
            m = l + (r-l) // 2
            value,time = current_list[m]
            if  time < timestamp:
                result = value
                l = m+1
            elif time > timestamp:
                r = m -1
            else:
                return value
        
        return result

