class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sen in sentences:
            max_words = max(max_words, len(sen.split()))

        return max_words

    def count_spaces(self, s):
        return s.count(' ') + 1

    def mostWordsFoundBetter(self, sentences: List[str]) -> int:
        max_words = 0
        for sen in sentences:
            max_words = max(max_words, self.count_spaces(sen))

        return max_words

