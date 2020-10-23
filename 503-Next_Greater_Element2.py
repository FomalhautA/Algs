class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, stack = [], nums[::-1]
        for n in nums[::-1]:
            while stack and stack[-1] <= n:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(n)

        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 2, 4, 5]
    ans = s.nextGreaterElements(nums)
    print(ans)
