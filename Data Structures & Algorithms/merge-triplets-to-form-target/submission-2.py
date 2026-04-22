class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplet_bool = [False,False,False]
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]:
                triplet_bool[0] = True
            if triplet[1] == target[1]:
                triplet_bool[1] = True
            if triplet[2] == target[2]:
                triplet_bool[2] = True

        return triplet_bool[0] and triplet_bool[1] and triplet_bool[2]