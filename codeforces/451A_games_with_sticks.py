if __name__ == '__main__':
    n, m = map(int, input().split(" "))

    # if n == 1 or m == 1:
    #     print("Akshat")
    # elif (n * m) % 2 == 0:
    #     print("Malvika")
    # else:
    #     print("Akshat")
    if max(n, m) % 2 == 0:
        print("Malvika")
    else:
        print("Akshat")

