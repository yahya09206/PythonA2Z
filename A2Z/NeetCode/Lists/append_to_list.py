from typing import List


def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    for n in elements:
        my_list.append(n)
    return my_list


print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))