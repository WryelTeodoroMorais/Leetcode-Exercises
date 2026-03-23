class Solution:
    def romanToInt(self, s: str) -> int:
        number = {'I':1, 'V':5, 'X':10,  'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)):
            if len(s) > i+1 and number[s[i]] < number[s[i+1]]:
                result-=number[s[i]]
            else:
                result+=number[s[i]]

        return result