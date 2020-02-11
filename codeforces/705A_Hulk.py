if __name__ == '__main__':
    n = int(input())
    relation = {
        0: "I love {}",
        1: "I hate {}"
    }

    for i in range(1, n+1):
        print(relation.get(i % 2).format("that" if i != n else "it"), end=" ")
