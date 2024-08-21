

def recursive_binary_search(start, end, array, target):
    if start > end:
        return False
    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    if array[middle] > target:
        return recursive_binary_search(start, middle - 1, array, target)
    return recursive_binary_search(middle + 1, end, array, target)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recursive_binary_search(start=0, end=len(lista) - 1, array=lista, target=5)) # 4
print(recursive_binary_search(start=0, end=len(lista) - 1, array=lista, target=11)) # False