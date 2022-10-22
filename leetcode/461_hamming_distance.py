class Solution:

    def get_bin(self, num):
        bin_list = []
        while num:
            bin_list.append(num % 2)
            num //= 2
        return bin_list

    def hammingDistance(self, x: int, y: int) -> int:
        bigger = max(x, y)
        smaller = min(x, y)
        b_b = self.get_bin(bigger)
        s_b = self.get_bin(smaller)
        h_d = 0
        s_len = len(s_b)
        for i, b in enumerate(b_b):
            if i < s_len:
                print(i, b, s_b[i])
                h_d += b ^ s_b[i]
            elif i >= s_len and b == 1:
                h_d += 1

        return h_d
