def get_groups():
    count = 1
    prev = magnets[0]
    for mag in magnets[1:]:
        if mag == prev:
            continue
        count += 1
        prev = mag

    return count


if __name__ == '__main__':
    n = int(input())
    count = 0
    prev = ''
    for i in range(n):
        mag = input()
        if mag == prev:
            continue
        count += 1
        prev = mag

    print(count)
