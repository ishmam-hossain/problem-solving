def capitalize(s):
    diff = 97 - 65
    res = ['']*len(s)

    for i in range(len(s)):
        _ascii = ord(s[i])
        if i == 0:
            if 97 <= _ascii <= 122:
                res[i] = chr(_ascii - diff)
            else:
                res[i] = s[i]
        else:
            if 65 <= _ascii <= 90:
                res[i] = chr(_ascii + diff)
            else:
                res[i] = s[i]

    return "".join(res)


def old_cAPS_Lock(s):
    res = ['']
    for i in range(len(s)):
        if i == 0:
            res.append(s[0])
            continue
        elif not s[i].isupper():
            return s
        res.append(s[i].lower())
    else:
        return "".join(res)


def cAPS_Lock(s):
    res = []
    is_all_caps = True

    for i in range(1, len(s), 1):
        if not s[i].isupper():
            is_all_caps = False
            break
    if is_all_caps:
        if s[0].isupper():
            return s.lower()
        else:
            return f"{s[0].upper()}{s[1:].lower()}"
    else:
        return s


if __name__ == '__main__':

    x = input()
    print(cAPS_Lock(x))
    # print(capitalize(x))
