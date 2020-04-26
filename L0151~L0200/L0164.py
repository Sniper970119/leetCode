# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃　　　　　　　    ┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""


class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        min_val, max_val, n = float('inf'), float('-inf'), len(nums)
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
            if nums[i] > max_val:
                max_val = nums[i]

        if min_val == max_val:
            return 0

        mins = [0] * (n + 1)
        maxs = [0] * (n + 1)
        has_num = [False] * (n + 1)

        for num in nums:
            index = int((num - min_val) * n / (max_val - min_val))
            mins[index] = num if not has_num[index] else min(mins[index], num)
            maxs[index] = num if not has_num[index] else max(maxs[index], num)
            has_num[index] = True

        max_len = 0
        m = maxs[0]
        for i in range(1, n + 1):
            if has_num[i]:
                curr_len = mins[i] - m
                if curr_len > max_len:
                    max_len = curr_len
                m = maxs[i]

        return max_len


if __name__ == '__main__':
    nums = [3, 6, 9, 1]
    print(Solution().maximumGap(nums))
