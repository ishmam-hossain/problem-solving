if __name__ == '__main__':
    steps = int(input())
    print(steps // 5 + (0 if steps % 5 == 0 else 1))
