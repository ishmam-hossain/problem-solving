def way_too_long_words(words):
    result = [word if len(word) <= 10 else f"{word[0]}{len(word) - 2}{word[-1]}" for word in words]
    return '\n'.join(result)


if __name__ == '__main__':
    n = int(input())
    words_list = [input() for _ in range(n)]
    print(way_too_long_words(words_list))
