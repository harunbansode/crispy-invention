def BinarySearch(n, l1):
    start = 0
    end = len(l1)
    middle = 0
    steps = 0

    while start <= end:
        print(f'steps : {steps}, : {list[start:end+1]}')
        steps = steps + 1
        middle = (start + end) // 2
        print(middle)

        if n == list[middle]:
            return middle
        elif n < middle:
            end = middle - 1
        else:
            start = middle + 1
    return -1


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
BinarySearch(target, lists)