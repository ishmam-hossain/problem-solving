def is_hello():
    target = "hello"

    if len(target) > len(s):
        return "NO"

    unq_chars = [s[0]]

    for i in range(1, len(s), 1):
        if s[i-1] != s[i]:
            unq_chars.append(s[i])

    # is_started = False
    # k = 0
    # for c in unq_chars:
    #     if not is_started:
    #         if c != target[k]:
    #             k += 1
    #         else:
    #             is_started = True
    #     else:
    #         if c != target[k]:
    #             k += 1




if __name__ == '__main__':
    s = input()
    print(is_hello())
