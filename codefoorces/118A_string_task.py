if __name__ == '__main__':
    s = input()
    vowels = ("a", "e", "i", "o", "u", "y")
    result = [f".{c}" for c in s.lower() if c not in vowels]

    print("".join(result))


