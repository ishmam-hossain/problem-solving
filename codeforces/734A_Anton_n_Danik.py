def get_winner():
    anton = 0
    danik = 0
    mid = n // 2
    for c in s:
        if c == 'A':
            anton += 1
            if anton > mid:
                return "Anton"
        else:
            danik += 1
            if danik > mid:
                return "Danik"
    else:
        return "Friendship"


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(get_winner())
