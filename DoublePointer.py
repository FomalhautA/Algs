
def rain1d(a):
    res = 0
    n = len(a)

    left = 0
    right = n-1

    l_max = a[left]
    r_max = a[right]

    while left <= right:
        l_max = max(l_max, a[left])
        r_max = max(r_max, a[right])

        if l_max < r_max:
            res += l_max - a[left]
            left += 1
        else:
            res += r_max - a[right]
            right -= 1

    return res


if __name__ == '__main__':
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(rain1d(a))
