def are_anagrams(*args):
    if len(args) < 2:
        return False
    sorted_words = [''.join(sorted(word)) for word in args]
    return all(word == sorted_words[0] for word in sorted_words[1:])


if __name__ == "__main__":
    words = input().split()
    print(are_anagrams(words))
