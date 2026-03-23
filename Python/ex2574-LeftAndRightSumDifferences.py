class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, final = [], []
        soma1, soma2 = 0, 0
        for i in nums:
            leftSum.append(soma1)
            soma1+=i

        cont = len(nums)-1
        for i in nums[::-1]:
            final.insert(0, abs(leftSum[cont] - soma2))
            soma2+=i
            cont-=1

        return final