def fun_print(n):
    l = n * 2

    for x in range(n):
        for i in range(0, l-1, 1):
            if i < n:
                if l-n-i <= x:
                    print(" ", end=" ")
                else:
                    print(l - n - i, end=" ")
            else:
                if i-n+2 <= x:
                    print(" ", end=" ")
                else:
                    print(i-n+2, end=" ")

        print()


if __name__ == '__main__':
    n = int(input())
    fun_print(n)


"""
INPUT: 
5

OUTPUT:
543212345
5432 2345
543   345
54     45
5       5


"""


"""
ACCIDENT!!!


5 4 3   1   3 4 5 
5 4 3 2   2 3 4 5 
5 4 3   1   3 4 5 
5 4   2 1 2   4 5 
5   3 2 1 2 3   5 


def fun_print(n):
    l = n * 2

    for x in range(n):
        for i in range(0, l-1, 1):
            if l-n-i == x or i-n+2 == x:
                print(" ", end=" ")
                continue
            print(l-n-i if i < n else i-n+2, end=" ")

        print()

"""