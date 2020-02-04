def hq9_lang(s):
    commands = ('H', 'Q', '9')
    for c in s:
        if c in commands:
            return "YES"
    return "NO"


if __name__ == '__main__':
    x = input()
    print(hq9_lang(x))
