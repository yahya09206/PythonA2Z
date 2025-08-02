def concatenate(word1: str, word2: str) -> str:
    if len(word1 + word2) > 10:
        return "Too long!"
    else:
        return word1 + word2


print(concatenate("He", "llo"))
print(concatenate("Lengths", "of10"))