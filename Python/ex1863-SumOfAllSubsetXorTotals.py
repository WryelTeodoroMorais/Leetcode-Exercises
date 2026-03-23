class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total = total | i

        return total * pow(2, len(nums) - 1)