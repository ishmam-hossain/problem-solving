class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        res = [None]*len(word_list)
        for word in word_list:
            res[int(word[-1]) - 1] = word[:-1]
        
        return ' '.join(res)
