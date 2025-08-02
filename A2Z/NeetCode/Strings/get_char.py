def print_first_char(word: str) -> None:
    print(word[0])

def print_second_char(word: str) -> None:
    print(word[1])

def print_third_char(word: str) -> None:
    last_index = len(word) -1
    print(word[last_index])


print_first_char("hello")
print_third_char("word")