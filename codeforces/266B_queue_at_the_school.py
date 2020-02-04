def restructure_queue(s, n):
    q = list(s)
    for _ in range(n):
        for i in range(len(s)-1):
            if s[i] < s[i+1]:
                q[i+1], q[i] = q[i], q[i+1]
        s = "".join(q)

    return "".join(q)


if __name__ == '__main__':
    n, t = map(int, input().split(" "))
    seq = input()
    print(restructure_queue(seq, t))
