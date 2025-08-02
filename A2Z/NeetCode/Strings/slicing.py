def get_substring(input_string: str, start: int, end: int) -> str:

    if end == -1:
        return ""
    else:
        return input_string[start:end]


print(get_substring("Hello world!", 1,4))