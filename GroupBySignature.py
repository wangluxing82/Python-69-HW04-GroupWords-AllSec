def group_by_signature(words: list) -> list:
    import collections
    grouped_words = collections.defaultdict(list)
    for word in words: 
        if not word:
            continue
        signature = "".join(sorted(word))
        grouped_words[signature].append(word)
    return list(grouped_words.values())

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
