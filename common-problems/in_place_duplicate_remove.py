# a = [1, 1, 2, 2, 2, 3, 4, 5, 5]
a = [5, 5, 5, 5, 89, 123, 123, 321, 321, 321, 4343]

j = 1

for i in range(1, len(a), 1):
    if a[i] != a[i-1]:
        a[j] = a[i]
        j += 1

print(a[:j])
