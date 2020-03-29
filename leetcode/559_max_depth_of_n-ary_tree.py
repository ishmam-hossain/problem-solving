class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0

        def get_max_depth(head, depth):
            if head is None:
                return depth

            for c_node in head.children:
                self.max_depth = max(get_max_depth(c_node, depth + 1), self.max_depth)

        get_max_depth(root, 0)

        return self.max_depth


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = int(line)

            ret = Solution().maxDepth(root)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

