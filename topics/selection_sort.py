def selection(lst: list[int]) -> list[int]:
    i: int = 0
    n: int = len(lst)
    while i < n:
        min_index: int = i
        j: int = i + 1
        while j < n:
            if lst[j] < lst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
        i += 1
    return lst

lst: list[int] = [25,23,35,47,41,27,4,24,15,37]

result: list[int] = selection(lst)

print(result)
