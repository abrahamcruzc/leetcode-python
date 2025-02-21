def bubble(list_a: list[int]) -> list[int]:
    n: int = len(list_a)
    while True:
        swap_counter: int = 0
        for i in range(n - 1):
            if list_a[i] > list_a[i + 1]:
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                swap_counter += 1
        n -= 1
        print(list_a)
        if swap_counter == 0:
            break

    return list_a

list_a: list[int] = [9,8,7,6,5,4,3,2,1]
result: list[int] = bubble(list_a)
print(f'Final list: {result}')
