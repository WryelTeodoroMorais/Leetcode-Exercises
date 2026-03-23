class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {m:0 for m in nums}
        for j in nums:
            result[j] += 1

        for k, i in result.items():
            if i == 1:
                return k