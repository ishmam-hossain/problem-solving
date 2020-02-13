if __name__ == '__main__':
    s = input()
    res = set()
    ignore = ('{', '}', ',', ' ')
    for c in s:
        if c not in ignore:
            res.add(c)

    print(len(res))
