class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }
        return sum([ops.get(op) for op in operations])

    def finalValueAfterOperationsOptimized(self, operations: List[str]) -> int:
        ops = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }
        res = 0
        for op in operations:
            res += ops.get(op)
        return res

    def finalValueAfterOperationsMoreOptimized(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            res += 1 if (op[0] == "+" or op[-1] == "+") else -1
        return res


