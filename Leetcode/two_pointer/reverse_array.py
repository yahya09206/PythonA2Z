def reverse_array(arr: int) -> int:

    l = 0
    r = len(arr) - 1

    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
