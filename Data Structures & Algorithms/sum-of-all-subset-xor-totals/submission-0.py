class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        XOR_SUM = 0
        def dfs(XOR,i):
            if i == len(nums):
                nonlocal XOR_SUM
                XOR_SUM += XOR
                return
            dfs(XOR^nums[i],i+1)
            dfs(XOR,i+1)
        
        dfs(0,0)
        return XOR_SUM
