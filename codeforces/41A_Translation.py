def translate():
    if len(s) != len(t):
        return "NO"
    length = len(s)
    for i in range(length):
        if s[i] != t[length-i-1]:
            return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    s = input()
    t = input()
    print(translate())

