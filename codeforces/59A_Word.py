def represent_word():
    cap_count = 0
    small_count = 0
    for c in s:
        if c.isupper():
            cap_count += 1
        else:
            small_count += 1
    return s.upper() if cap_count > small_count else s.lower()


if __name__ == '__main__':
    s = input()
    print(represent_word())

