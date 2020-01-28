if __name__ == '__main__':
    n = int(input())
    result = 0

    for _ in range(n):
        sure_solve_count = sum(map(int, input().split(" ")))
        result += 1 if sure_solve_count >= 2 else 0

    print(result)



