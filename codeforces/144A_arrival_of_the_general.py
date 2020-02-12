if __name__ == '__main__':
    n = int(input())
    soldiers = list(map(int, input().split(" ")))

    max_height_index = 0
    min_height_index = 0

    for i, height in enumerate(soldiers):
        if height > soldiers[max_height_index]:
            max_height_index = i
        if height <= soldiers[min_height_index]:
            min_height_index = i

    if min_height_index < max_height_index:
        max_height_index -= 1

    print((max_height_index - 0) + (n - 1 - min_height_index))
