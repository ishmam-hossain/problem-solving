def lengthOfLongestSubstring(s: str) -> int:
    visited = set()
    start = 0
    end = 0
    longest = 0

    while end < len(s):
        if s[end] not in visited:
            visited.add(s[end])
            end += 1
            longest = max(longest, len(visited))
        else:
            visited.remove(s[start])
            start += 1

    return longest


print(lengthOfLongestSubstring("dvdf"))
