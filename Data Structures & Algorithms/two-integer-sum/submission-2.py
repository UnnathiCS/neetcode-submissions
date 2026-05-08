class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            diff=target-nums[i]
            if diff in nums and nums.index(diff)!=i:
                return sorted([i,nums.index(diff)])
                