class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        if len(word_list) != len(pattern):
            return False

        key_to_value = dict()
        value_to_key = dict()

        for key, word in zip(pattern, word_list):
            if key_to_value.get(key) == word and value_to_key.get(word) == key:
                continue

            if (key in key_to_value and key_to_value.get(key) != word) or (
                    word in value_to_key and value_to_key.get(word) != key):
                return False

            key_to_value[key] = word
            value_to_key[word] = key

        return True


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
