l1 = [1, 5, 7, 7, 7, 7, 7, 7, 7, 7, 1, 3, 6, 6, 3, 4, 2, 6,6,6,6,6,6,6,6,6,6,6,6,6]

appear_dict = {}
for n in l1:
    appear_dict[n] = appear_dict.get(n, 0) + 1

most_repeat = l1[0]
for key, val in appear_dict.items():
    most_repeat = key if val > most_repeat else most_repeat

print(most_repeat)
