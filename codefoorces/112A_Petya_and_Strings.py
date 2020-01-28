def lexicographical_comparison():
    for i, c in enumerate(f_s):
        if c < l_s[i]:
            return -1
        elif c > l_s[i]:
            return 1
    else:
        return 0


if __name__ == '__main__':
    f_s = input().lower()
    l_s = input().lower()

    print(lexicographical_comparison())


