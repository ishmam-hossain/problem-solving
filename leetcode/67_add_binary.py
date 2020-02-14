def add_binary_string(a, b):
    if len(a) > len(b):
        b = b.zfill(len(a))
    else:
        a = a.zfill(len(b))

    mx_ln = len(a)

    _carry = 0
    _sum = []

    for i in range(len(a)):
        a_i = int(a[mx_ln - 1 - i])
        b_i = int(b[mx_ln - 1 - i])

        _sum.append(str(a_i ^ b_i ^ _carry))
        _carry = (a_i & b_i) | (b_i & _carry) | (a_i & _carry)

    if _carry:
        _sum.append(str(_carry))

    return "".join(_sum[::-1])


if __name__ == '__main__':
    print(add_binary_string('100001', '1111111'))
