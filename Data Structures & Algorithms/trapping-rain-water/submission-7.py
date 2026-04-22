class Solution:
    def trap(self, height: List[int]) -> int:
        leftprefix_arr = [0]*len(height)
        rightprefix_arr = [0]*len(height)
        leftprefix = 0
        rightprefix = 0

        for i in range(1,len(height)):
            leftprefix = max(leftprefix,height[i-1])
            leftprefix_arr[i] = leftprefix

            rightprefix = max(rightprefix,height[len(height)-i])
            rightprefix_arr[len(height)-i-1] = rightprefix

        print(leftprefix_arr)
        print(rightprefix_arr)

        result = 0

        for i in range(len(height)):
            water = max(min(leftprefix_arr[i],rightprefix_arr[i]) - height[i],0)
            print(i,water)
            result += water
        return result