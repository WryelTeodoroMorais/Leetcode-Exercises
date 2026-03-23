class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aux = []
        result = 0
        for i in s:
            if i in aux:
                index = aux.index(i)
                aux = aux[index + 1:]
            
            aux.append(i)
            result = max(result, len(aux))
        
        return result