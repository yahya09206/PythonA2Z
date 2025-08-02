#left is starting index, right side is ending index
def first_n_characters(s: str, n: int) -> str:
    return s[:n]

def last_n_characters(s: str, n: int) -> str:
    index = len(s) - n
    return s[index:]


print(first_n_characters("Neetcode", 3))
print(first_n_characters("Neetcode", 4))
print(first_n_characters("Neetcode", 8))
print(last_n_characters("Neetcode", 3))
print(last_n_characters("Neetcode", 4))
print(last_n_characters("Neetcode", 8))
