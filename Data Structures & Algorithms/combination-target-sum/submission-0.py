class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.tree(0,nums,target,[],[])

    def tree(self,i,nums,target,curr_list,ans):

        if sum(curr_list) == target:
            ans.append(curr_list[:])
            return
        if i >= len(nums) or sum(curr_list) > target:
            return

       
        curr_list.append(nums[i])
        self.tree(i,nums,target,curr_list,ans)
        curr_list.pop()
        
        self.tree(i+1,nums,target,curr_list,ans)

        return ans