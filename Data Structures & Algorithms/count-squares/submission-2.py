class CountSquares:

    def __init__(self):
        self.my_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.my_map[(point[0],point[1])] += 1

        
    def count(self, point: List[int]) -> int:
        
        px = point[0]
        py = point[1]
        count = 0
        for (x,y),freq in self.my_map.items():
            if abs(px-x) == abs(py-y) and (px,py) != (x,y):
                if (x,py) in self.my_map and (px,y) in self.my_map:
                    count += freq * self.my_map[x,py] * self.my_map[px,y]
                
        return count

        
