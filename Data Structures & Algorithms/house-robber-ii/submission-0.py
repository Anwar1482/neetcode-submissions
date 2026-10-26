class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0]*len(nums)
        dp2 = [0]*len(nums)

        dp1[0] = 0
        dp1[1]= nums[1]
        
        dp2[0] = nums[0]
        dp2[1] = max(dp2[0], nums[1])
        for n in range(2,len(nums)):
            dp1[n] = max(dp1[n-1],dp1[n-2]+nums[n])
            dp2[n] = max(dp2[n-1], dp2[n-2]+nums[n])
        return max(dp1[-1], dp2[len(nums)-2])