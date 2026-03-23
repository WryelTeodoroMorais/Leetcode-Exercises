class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d, e = set(), set()
        result = []
        for i in range(len(A)):
            d.add(A[i])
            e.add(B[i])
            common = len(d & e)
            result.append(common)

        return result