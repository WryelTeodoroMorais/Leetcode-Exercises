class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        soma = 0
        for i in range (len(nums)):
            if i % 2 == 0:
                soma += nums[i]
            else:
                soma -= nums[i]

        return soma

                
