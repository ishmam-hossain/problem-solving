if __name__ == '__main__':
    n = int(input())
    tot_passengers = 0
    max_passengers = -99

    for _ in range(n):
        exits, entered = map(int, input().split(" "))
        tot_passengers -= exits
        tot_passengers += entered

        if tot_passengers > max_passengers:
            max_passengers = tot_passengers

    print(max_passengers)


