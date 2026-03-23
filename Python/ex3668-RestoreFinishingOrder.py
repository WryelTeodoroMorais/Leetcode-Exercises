class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        aux = set (friends)
        result = []
        for i in order:
            if i in aux:
                result.append(i)

        return result

        