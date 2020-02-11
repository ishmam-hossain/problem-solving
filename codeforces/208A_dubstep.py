if __name__ == '__main__':
    s = input()
    pattern = "WUB"
    space_printed = True

    while s:
        if s[:3] == pattern:
            s = s[3:]
            if not space_printed:
                print(" ", end="")
                space_printed = True

        else:
            print(s[0], end='')
            s = s[1:]
            space_printed = False
