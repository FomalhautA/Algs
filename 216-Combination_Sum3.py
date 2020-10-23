class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def combination(k, n, nums):
            if n == 0 and k == 0:
                return []
            if n < 0 or k == 0 or len(nums) == 0:
                return None

            ans = []
            for i in range(len(nums)):
                if n-nums[i] < 0:
                    break
                temp = combination(k - 1, n - nums[i], nums[i + 1:])
                if temp is not None:
                    if len(temp) == 0:
                        ans.append([nums[i]])
                    else:
                        for item in temp:
                            ans.append([nums[i]] + item)
            if len(ans) == 0:
                return None
            else:
                return ans

        nums = range(1, 10)

        return combination(k, n, nums)


if __name__ == '__main__':
    s = Solution()
    k, n = 3, 7
    ans = s.combinationSum3(k, n)
    print(ans)
