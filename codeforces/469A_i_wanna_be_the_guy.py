def lets_see():
    if p + x < n:
        return "Oh, my keyboard!"

    for i in range(1, n + 1):
        if i not in p_tasks and i not in x_tasks:
            return "Oh, my keyboard!"
    else:
        return "I become the guy."


if __name__ == '__main__':
    n = int(input())
    p, *p_tasks = map(int, input().split(" "))
    x, *x_tasks = map(int, input().split(" "))

    print(lets_see())
