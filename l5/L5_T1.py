def prefix(str):
    if not str:
        return ""
    min_word = min(str, key=len)
    for i, symb in enumerate(min_word):
        for word in str:
            if word[i] != symb:
                return min_word[:i]
    return min_word


if __name__ == "__main__":
    words = input().split()
    print(prefix(words))
