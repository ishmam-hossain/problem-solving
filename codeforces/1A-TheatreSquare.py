def theatre_square():
    if n == m == a:
        return 1

    result = 0
    result += n // a + (1 if n % a > 0 else 0)
    result += m // a + (1 if m % a > 0 else 0)
    return result


if __name__ == '__main__':
    n, m, a = map(int, input().split(" "))
    print(theatre_square())



"""
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    
    0 0

"""