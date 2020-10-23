
def quick_sort(a, low, high):
    """

    :param a:
    :return:
    """
    if low >= high:
        return

    key = a[low]
    left = low
    right = high

    while left < right:
        while left < right and a[right] >= key:
            right -= 1

        a[left] = a[right]

        while left < right and a[left] <= key:
            left += 1

        a[right] = a[left]

    a[left] = key

    quick_sort(a, low, left-1)
    quick_sort(a, left+1, high)


def swap(a, idx1, idx2):
    temp = a[idx1]
    a[idx1] = a[idx2]
    a[idx2] = temp
    return


def max_heapify(a, start, end):
    dad = start
    son = dad*2+1
    while son <= end:
        if son+1 <= end and a[son] < a[son+1]:
            son += 1
        if a[dad] >= a[son]:
            return
        else:
            swap(a, dad, son)
            dad = son
            son = dad*2+1


def heap_sort(a):
    """

    :param a:
    :return:
    """
    l = len(a)

    for i in reversed(range(l // 2)):
        max_heapify(a, i, l-1)

    for i in reversed(range(1, l)):
        swap(a, 0, i)
        max_heapify(a, 0, i-1)


def merge(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    temp = []
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    while i < la and j < lb:
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1

    if i < la:
        temp.extend(a[i:])
    if j < lb:
        temp.extend(b[j:])

    return temp


def merge_sort(a):
    """

    :param a:
    :return:
    """
    merge_lst = [[item] for item in a]

    while len(merge_lst) > 1:
        l = len(merge_lst)
        i = 0
        temp = []
        while i+1 < l:
            temp.append(merge(merge_lst[i], merge_lst[i+1]))
            i += 2
        merge_lst = temp

    return merge_lst[0]


if __name__ == '__main__':
    a = [2, 1, 4, 2, 3, 9, 4, 2]

    quick_sort(a, 0, len(a)-1)

    print(a)

    a = [2, 1, 4, 2, 3, 9, 4, 2]
    heap_sort(a)
    print(a)

    a = [2, 1, 4, 2, 3, 9, 4, 2]
    b = merge_sort(a)
    print(b)

