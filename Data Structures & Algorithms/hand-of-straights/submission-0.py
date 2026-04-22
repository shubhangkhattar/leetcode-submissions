class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        heapq.heapify(hand)

        count = Counter(hand)

        for num in hand:
            if count[num]:
                for i in range(num,num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        
        return True

        



        


