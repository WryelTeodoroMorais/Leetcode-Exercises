class Solution:
    def maxFreqSum(self, s: str) -> int:
        vog = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        cons = {c: 0 for c in 'bcdfghjklmnpqrstvwxyz'}

        for ch in s:
            if ch in vog:
                vog[ch] += 1
            elif ch in cons:
                cons[ch] += 1

        return max(vog.values()) + max(cons.values())

        