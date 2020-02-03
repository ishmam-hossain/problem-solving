def get_count(teams):
    counter = {}
    for team in teams:
        counter[team] = counter.get(team, 0) + 1

    result = 0

    if 4 in counter:
        result = counter[4]
        counter[4] = 0

    if 2 in counter:
        if counter[2] % 2 == 0:
            result += counter[2] // 2
            counter[2] = 0
        else:
            result += counter[2] - 1
            counter[2] = 1
    if 3 in counter and 1 in counter:
        if counter[3] == counter[1]:
            result += counter[3]
            counter[3] = counter[1] = 0

    if 1 in counter and 2 in counter:
        if counter[1] == counter[2]:
            result += counter[1]
            counter[1] = counter[2] = 0

    if 3 in counter:
        result += counter[3]
        counter[3] = 0

    if 1 in counter:
        result += counter[1] // 4 if counter[1] % 4 == 0 else (counter[1] // 4) + 1
        counter[1] = 0

    for key in counter:
        result += counter[key]

    print(counter)
    print(result)


def new_way(a):
    taxi_count = 0
    unvisited = []
    a = sorted(a)[::-1]

    start = 0
    end = len(a) - 1

    while start <= end:
        temp = a[start] + a[end]
        if start >= end:
            return taxi_count + 1

        elif temp == 4:
            taxi_count += 1
            start += 1
            end -= 1

        elif temp > 4:
            taxi_count += 1
            start += 1

        elif temp < 4:
            while end > start and temp <= 4:
                if temp == 4:
                    taxi_count += 1

                print("in < ", start, end, a[start], a[end], "temp -> ", temp)
                end -= 1
                temp += a[end]
            temp = 0

            return taxi_count

    return taxi_count


def min_taxi(a):
    return sum(a) // 4 + (1 if sum(a) % 4 != 0 else 0)


def new_strategy(a):
    taxi_count = 0
    unvisited = []
    a = sorted(a)[::-1]
    print("after sort --> ", a)

    start = 0
    end = len(a) - 1

    while start <= end:
        temp = a[start] + a[end]
        # if start >= end:
        #     return taxi_count + 1

        if temp == 4:
            a[start] = a[end] = -1
            taxi_count += 1
            start += 1
            end -= 1

        elif temp > 4:
            a[start] = -1
            taxi_count += 1
            start += 1

    print("after processing --> ", a)

            
if __name__ == '__main__':
    while 1:
        n = int(input())
        team_list = list(map(int, input().split(" ")))
        # print(min_taxi(team_list))
        # print(new_way(team_list))
        print(new_strategy(team_list))


"""
After the lessons n groups of schoolchildren went outside and decided to visit Polycarpus to celebrate his birthday.
We know that the i-th group consists of si friends (1 ≤ si ≤ 4), and they want to go to Polycarpus together. 
They decided to get there by taxi. Each car can carry at most four passengers. 

What minimum number of cars will the children need if all members of each group
should ride in the same taxi (but one taxi can take more than one group)?

Input
The first line contains integer n (1 ≤ n ≤ 105) — the number of groups of schoolchildren. 
The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). 
The integers are separated by a space, si is the number of children in the i-th group.

Output
Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.


______________________________________________________

Examples
----------------------------------
input
----------------------------------
5
1 2 4 3 3
----------------------------------
output
4
----------------------------------
----------------------------------
input
----------------------------------
8
2 3 4 4 2 1 3 1
----------------------------------
output
5


Note
----------------------------------
In the first test we can sort the children into four cars like this:

the third group (consisting of four children),
the fourth group (consisting of three children),
the fifth group (consisting of three children),
the first and the second group (consisting of one and two children, correspondingly).
There are other ways to sort the groups into four cars.



"""

"""
4 3 3 2 1
3 3 2 1



1 2 4 3 3
1 2 3 3
2 3
3
2

"""
