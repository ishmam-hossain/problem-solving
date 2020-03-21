def count_one(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count


print(count_one(21))
