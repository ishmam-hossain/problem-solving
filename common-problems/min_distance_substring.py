def MinWindowSubstring(strArr):
    source = strArr[0]
    pattern = strArr[1]

    if not len(source) > len(pattern):
        return ""

    result = source

    for i, c in enumerate(source):
        if c in pattern:
            sub_str = source[i:]
            ptr = list(pattern)

            if len(sub_str) > len(pattern):
                for j, x in enumerate(sub_str):
                    try:
                        ptr[ptr.index(x)] = -1
                        print(ptr)
                    except ValueError:
                        pass

                    try:
                        _sum = sum(ptr)
                        if len(sub_str[:j + 1]) < len(result):
                            result = sub_str[:j + 1]
                            break
                    except TypeError:
                        pass
            break

    return result


# keep this function call here
print(MinWindowSubstring(input()))