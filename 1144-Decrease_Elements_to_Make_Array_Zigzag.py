import copy


class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 0 if nums[0] != nums[1] else 1

        temp = []
        for peak in [True, False]:
            nums_init = copy.deepcopy(nums)
            count = 0
            i = 0
            while i < len(nums_init) - 1:
                if peak:
                    if nums_init[i] <= nums_init[i + 1]:
                        count += nums_init[i + 1] - nums_init[i] + 1
                        nums_init[i + 1] = nums_init[i] - 1
                else:
                    if nums_init[i] >= nums_init[i + 1]:
                        count += nums_init[i] - nums_init[i + 1] + 1
                        nums_init[i + 1] = nums_init[i] + 1
                i += 1
                peak = not peak

            temp.append(count)

        return min(temp)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 4, 4, 10, 10, 6, 2, 3]

    steps = s.movesToMakeZigzag(nums)

    print(steps)
