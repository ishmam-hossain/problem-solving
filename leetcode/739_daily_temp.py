
// This is a valid solution but gets TLE for huge inputs
// Time - O(n^2)
// Space - O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        for i, t1 in enumerate(temperatures):
            for j, t2 in enumerate(temperatures[i:], i):
                if t2 > t1:
                    answer[i] = j - i
                    break
        return answer
