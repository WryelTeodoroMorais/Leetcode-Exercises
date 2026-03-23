class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if (complemento) in aux:
                return [aux[complemento], i]
            aux[num] = i