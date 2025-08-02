def remove_fourth_character(word: str) -> str:
    first_part = word[:3]
    second_part = word[4:]
    return first_part + second_part


print(remove_fourth_character("Neetcode"))
