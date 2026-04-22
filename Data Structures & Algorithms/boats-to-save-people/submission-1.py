class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        left = 0
        right = len(people) - 1
        count = 0

        while left <= right:
            total =  people[left] + people[right]
            if left<right and  total <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                right -= 1
        
        return count


        # 1,2,4,5

        # 6