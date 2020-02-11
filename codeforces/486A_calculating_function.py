if __name__ == '__main__':
    n = int(input())
    no_of_odds = (n // 2) + (1 if n % 2 != 0 else 0)
    sum_of_odd = -1 * no_of_odds ** 2

    n -= no_of_odds
    sum_of_even = (n * (n+1))

    print(sum_of_even + sum_of_odd)
