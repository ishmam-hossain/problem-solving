def get_max():
    max_val = a * b * c
    max_val = max(max_val, ((a+b) * c))
    max_val = max(max_val, (a * (b + c)))
    max_val = max(max_val, (a + b + c))

    return max_val


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(get_max())
