def insertion(lst: list[int]) -> list[int]:
    n: int = len(lst)
    i: int = 1
    for i in range(1, n):
        current_value: int = lst[i]
        j: int = i - 1
        while j >= 0 and lst[j] > current_value :
            lst[j + 1] = lst[j] # Desplaza a la derecha 
            j -= 1
        lst[j + 1] = current_value
        i += 1
    return lst


lst: list[int] = [10,5,24,13,49,43,27,37,39,41]

result: list[int] = insertion(lst)
print(result)
