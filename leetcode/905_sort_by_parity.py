class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        for n in A:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds

