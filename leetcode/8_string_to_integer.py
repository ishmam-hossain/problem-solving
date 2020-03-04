class Solution:
    def myAtoi(self, str: str) -> int:
        my_num = 0
        pos = 0
        is_neg = False
        is_pos = False
        entered = False
        got_out = False
        INT_MIN = -2**31
        INT_MAX = 2 ** 31 - 1

        for c in str[::-1]:
            ascii_val = ord(c)
            if 48 <= ascii_val <= 57:
                my_num += ord(c) % 48 * 10 ** pos
                pos += 1
                entered = True
            elif entered:
                got_out = True

            if c == '.':
                my_num = 0
                entered = False
                got_out = False
                pos = 0

            if c == '-' and entered and got_out:
                is_neg = True

            if c == '+' and entered and got_out:
                is_pos = True

            if entered and got_out and c not in ('-', '+', ' '):
                entered = got_out = is_pos = is_neg = False
                # my_num = 0

            if is_neg and is_pos:
                return 0

        my_num = my_num if not is_neg else my_num * -1

        if my_num < INT_MIN:
            return INT_MIN
        elif my_num > INT_MAX:
            return INT_MAX

        return my_num

    def new_way(self, str):
        str = str.strip()
        if str[0].isnumeric() or str[0] not in ('-', '+'):
            return 0

        is_started = False
        arr = []

        for c in str[1:]:
            if not c.isdigit() and is_started:
                return sum([n * 10 ** i for i, n in enumerate(arr[::-1])])
            is_started = True
            arr.append(int(c))

        return sum([n * 10 ** i for i, n in enumerate(arr[::-1])])


s = Solution()
# print(s.myAtoi("  -0012a42"))
print(s.new_way("  -0012a42"))
print(s.new_way("  12a42"))
