class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preFixSum = 0
        prefixMap = defaultdict(int)
        prefixMap[0] = 1
        result = 0

        for num in nums:
            preFixSum += num
            result += prefixMap[preFixSum-k] 
            prefixMap[preFixSum] += 1
        
        return result




# # [2,-1,1,2]
# #         |

# sum = 4

# {0:1}{2:2}{1:1}

4