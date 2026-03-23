class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sinal = 1
        else:
            sinal = 0

        s = abs(x)
        t = str(s)
        x = [i for i in t][::-1]

        result = int("".join(x))

        if result > abs(pow(2,31)):
            return 0

        if sinal == 1:
            return -result
        else:
            return result
