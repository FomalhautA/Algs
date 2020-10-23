class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def swap(a, idx1, idx2):
            temp = a[idx1]
            a[idx1] = a[idx2]
            a[idx2] = temp

        def max_heapify(a, start, end):
            dad = start
            son = dad * 2 + 1

            while son <= end:
                if son + 1 <= end and a[son + 1] > a[son]:
                    son += 1
                if a[son] <= a[dad]:
                    return
                else:
                    swap(a, dad, son)
                    dad = son
                    son = dad * 2 + 1

        for i in reversed(range(len(nums) // 2)):
            max_heapify(nums, i, len(nums) - 1)

        for i in reversed(range(len(nums) - k, len(nums))):
            swap(nums, 0, i)
            max_heapify(nums, 0, i - 1)

        return nums[-k]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    res = s.findKthLargest(nums, 2)
    print(res)

