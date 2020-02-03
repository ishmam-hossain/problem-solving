def make_lucky_numbers():
    lucky_digits = (4, 7)
    lucky_numbers = []

    number_of_digits = 3
    for i in range(0, number_of_digits + 1):
        for k in range(len(lucky_digits)):
            while i >= 0:
                num = lucky_digits[k] * (10 ** i)
                print(num)
                i += 1
        print("----------")


make_lucky_numbers()


"""
1.             num = lucky_digits[k] * (10 ** i) + (lucky_digits[abs(1-k)] if i > 0 else 0)
"""