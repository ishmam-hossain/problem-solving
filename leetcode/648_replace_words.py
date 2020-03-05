class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        word_list = sentence.split()
        sorted_dict = sorted(dict, key=len)
        for i, word in enumerate(word_list):
            for root in sorted_dict:
                if word.startswith(root):
                    word_list[i] = root
                    break

        return " ".join(word_list)