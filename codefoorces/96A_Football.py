def is_dangerous():
    count = 1
    for i in range(1, len(formation) + 1, 1):
        if i < len(formation):
            if formation[i] == formation[i-1]:
                count += 1
                if count >= 7:
                    return "YES"
            else:
                count = 1
    else:
        return "NO"


if __name__ == '__main__':
    formation = input()
    print(is_dangerous())


