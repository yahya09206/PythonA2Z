def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) > len(word2):
        return word1
    elif len(word1) == len(word2):
        return word1
    else:
        return word2


print(get_longer_word("bike", "mike"))