class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        index_pairs = []
        min_index = 99999999999999999

        for i, res in enumerate(list1):
            d[res] = i

        for i, res in enumerate(list2):
            if res in d:
                index_pairs.append((i, d[res]))
                min_index = min(min_index, i + d[res])

        res = [list2[pair[0]] for pair in index_pairs if sum(pair) == min_index]

        return res