class Solution:
    vals = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    def try_new(self, num):
        res = []
        closest = 999999999999999999999999999999
        for n in list(self.vals.keys())[::-1]:
            closest = int(min((num / n), closest)) * n
            print(closest)
        print(closest)

    def get_closes_keys(self, key):
        all_keys = list(self.vals.keys())
        length = len(self.vals.keys())
        for i, dict_key in enumerate(all_keys):
            if i + 1 < length:
                if dict_key < key < all_keys[i+1]:
                    return dict_key, all_keys[i+1]

    def intToRoman(self, num: int) -> str:
        res = []
        while num:
            digit = num % 10
            num //= 10

            if digit in self.vals:
                res.append(self.vals[digit])
            else:
                lower, upper = self.get_closes_keys(key=digit)
                print(lower, upper)
                if upper - digit == 1:
                    res.extend([self.vals[upper], self.vals[lower]])
                else:
                    print("here")
                    res.extend([self.vals[lower]]*(digit-lower+1))

        return "".join(res[::-1])


s = Solution()
print(s.try_new(17))
