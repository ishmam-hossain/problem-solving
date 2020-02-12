if __name__ == '__main__':
    n = int(input())
    prob_status = input()

    for p in prob_status:
        if p == '1':
            print("HARD")
            break
    else:
        print("EASY")
