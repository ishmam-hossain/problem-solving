class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        cc = dict()
        for c in magazine:
            cc[c] = cc.get(c, 0) + 1


        pointer = 0
        for i, c in enumerate(ransomNote):
            if cc.get(c, 0) > 0:
                pointer = i
                cc[c] = cc[c] - 1
            else:a
                return False
        
        return pointer == (len(ransomNote) - 1)
    
