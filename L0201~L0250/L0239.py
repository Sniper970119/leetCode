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
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]
        if len(nums) == 2:
            if k != 1:
                return [max(nums[0], nums[1])]
            else:
                return nums
        res = []
        for i in range(len(nums) - k+1):
            _max = nums[i]
            for j in range(1, k):
                if _max < nums[i + j]:
                    _max = nums[i + j]
            res.append(_max)
        return res
        pass


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    nums = [5,3,4]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))
