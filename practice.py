
def quick_sort(a, start, end):
    if start >= end:
        return
    key = a[start]
    left = start
    right = end
    while left < right:
        while left < right and a[right] >= key:
            right -= 1
        a[left] = a[right]
        while left < right and a[left] <= key:
            left += 1
        a[right] = a[left]

    a[left] = key
    quick_sort(a, start, left-1)
    quick_sort(a, left+1, end)


def swap(a, idx1, idx2):
    temp = a[idx1]
    a[idx1] = a[idx2]
    a[idx2] = temp
    return


def max_heapify(a, start, end):
    if start >= end:
        return

    dad = start
    son = dad*2+1

    while son <= end:
        if son+1 <= end and a[son] < a[son+1]:
            son += 1
        if a[dad] < a[son]:
            swap(a, dad, son)
            dad = son
            son = dad*2+1
        else:
            return


def heap_sort(a):
    l = len(a)

    for i in reversed(range(l // 2)):
        max_heapify(a, i, l-1)

    for i in reversed(range(1, l)):
        swap(a, 0, i)
        max_heapify(a, 0, i-1)


if __name__ == '__main__':
    a = [2, 1, 4, 2, 3, 9, 4, 2]
    b = [2, 3, 5, 2, 1, 6, 3, 8, 10]
    c = []
    d = [2]
    quick_sort(a, 0, len(a)-1)
    print(a)
    quick_sort(b, 0, len(b)-1)
    print(b)
    quick_sort(c, 0, len(c)-1)
    print(c)
    quick_sort(d, 0, len(d)-1)
    print(d)

    a = [2, 1, 4, 2, 3, 9, 4, 2]
    b = [2, 3, 5, 2, 1, 6, 3, 8, 10]
    c = []
    d = [2]
    heap_sort(a)
    print(a)
    heap_sort(b)
    print(b)
    heap_sort(c)
    print(c)
    heap_sort(d)
    print(d)


