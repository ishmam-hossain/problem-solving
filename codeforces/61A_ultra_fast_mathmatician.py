if __name__ == '__main__':
    s1 = input()
    s2 = input()

    for i in range(len(s1)):
        print(int(s1[i]) ^ int(s2[i]), end="")
