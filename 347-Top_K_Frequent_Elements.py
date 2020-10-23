import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        def swap(a, idx1, idx2):
            temp = a[idx1]
            a[idx1] = a[idx2]
            a[idx2] = temp

        def max_heapify(a, b, start, end):
            dad = start
            son = dad * 2 + 1

            while son <= end:
                if son+1 <= end and a[son] < a[son + 1]:
                    son += 1
                if a[son] <= a[dad]:
                    return
                else:
                    swap(a, dad, son)
                    swap(b, dad, son)
                    dad = son
                    son = dad * 2 + 1

        mem = collections.defaultdict(int)
        for item in nums:
            mem[item] = mem.get(item, 0) + 1

        values = [item for item in mem.keys()]
        cnts = [mem[item] for item in mem.keys()]

        for i in reversed(range(len(cnts) // 2)):
            max_heapify(cnts, values, i, len(cnts) - 1)

        for i in reversed(range(len(cnts) - k, len(cnts))):
            swap(cnts, 0, i)
            swap(values, 0, i)
            max_heapify(cnts, values, 0, i - 1)

        ans = []
        for i in range(1, k+1):
            ans.append(values[-i])

        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    res = s.topKFrequent(nums, k)
    print(res)
