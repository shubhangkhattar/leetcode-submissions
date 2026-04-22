class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return self.tree(0,nums,[],ans)
        
        
    
    def tree(self,i,nums,curr_list,ans):
        
        if i >= len(nums):
            ans.append(curr_list[:])
            return
        
        self.tree(i+1,nums,curr_list,ans)
        curr_list.append(nums[i])
        self.tree(i+1,nums,curr_list,ans)
        curr_list.pop()

        return ans
