if __name__ == '__main__':
    n = int(input())
    numbers = map(int, input().split(" "))

    even_count = 0
    odd_count = 0
    last_even_index = -1
    last_odd_index = -1

    for i, n in enumerate(numbers):
        if n % 2 == 0:
            last_even_index = i
            even_count += 1
        else:
            last_odd_index = i
            odd_count += 1

    if even_count > odd_count:
        print(last_odd_index + 1)
    else:
        print(last_even_index + 1)
