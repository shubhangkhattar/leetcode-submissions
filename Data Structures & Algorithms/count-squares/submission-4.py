class CountSquares:

    def __init__(self):
        self.freq_map = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.freq_map[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        print(self.freq_map)
        px,py = point
        result = 0
        for (x,y),freq in self.freq_map.items():
            
            if (abs(px-x) == abs(py-y)) and  px != x and py != y:
                if (x,py) in self.freq_map and (px,y) in self.freq_map:
                    result += (self.freq_map[(px, y)] *
                        self.freq_map[(x, py)] *
                        freq)

        
        return result



        
