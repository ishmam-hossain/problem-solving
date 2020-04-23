class Solution:
    def compress(self, chars) -> int:
        cur = chars[0]
        i = j = count = 0

        while i < len(chars):
            if chars[i] != cur:
                if count == 1:
                    chars[j] = cur
                    j += 1
                else:
                    chars[j] = cur
                    j += 1
                    c_s = str(count)
                    for c in c_s:
                        chars[j] = c
                        j += 1

                cur = chars[i]
                count = 1

            else:
                count += 1

            i += 1

        if count == 1:
            chars[j] = cur
            j += 1
        else:
            chars[j] = cur
            j += 1
            c_s = str(count)
            for c in c_s:
                chars[j] = c
                j += 1

        print(chars)
        return j


s = Solution()
print(s.compress(["a", "a", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]))
print(s.compress(["a", "a", "a", "a", "a", "b"]))
