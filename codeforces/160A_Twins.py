def split_coin():
    weight = sorted(seq)[::-1]
    total_amt = sum(seq)
    taken = 0
    left = total_amt
    i = 0
    while taken <= left and i < len(weight):
        taken += weight[i]
        left = left - weight[i]
        i += 1

    return i


if __name__ == '__main__':
    total_coin = int(input())
    seq = list(map(int, input().split()))
    print(split_coin())
