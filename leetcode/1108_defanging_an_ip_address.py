class Solution:
    def defangIPaddr(self, address: str) -> str:
        final_ip = ""
        for c in address:
            c = c if c != "." else "[.]"
            final_ip = f"{final_ip}{c}"

        return final_ip


s = Solution()
print(s.defangIPaddr("198.167.12.11"))
