class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        words_list = S.split(" ")
        res = []

        for i, word in enumerate(words_list):
            if word.startswith(vowels):
                new_word = f"{word}ma{'a' * (i + 1)}"
            else:
                new_word = f"{word[1:]}{word[0]}ma{'a' * (i + 1)}"

            res.append(new_word)

        return " ".join(res)