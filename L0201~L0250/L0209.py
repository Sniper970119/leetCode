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


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if s > sum(nums):
            return 0
        left, right, res, sum_lr = 0, 0, len(nums) + 1, 0  # 双指针都从第一位出发
        while right < len(nums):
            while sum_lr < s and right < len(nums):  # sum_lr小则右指针右移
                sum_lr += nums[right]
                right += 1
            while sum_lr >= s and left >= 0:  # sum_lr大则左指针右移
                res = min(res, right - left)
                sum_lr -= nums[left]
                left += 1
        return res


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))
