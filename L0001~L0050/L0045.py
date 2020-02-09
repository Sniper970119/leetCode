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
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        step = 0
        end = 0
        max_bound = 0
        for i in range(len(nums) - 1):
            max_bound = max(max_bound, nums[i] + i)
            if (i == end):
                step += 1
                end = max_bound
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1]
    # nums = [1, 1, 1, 1]
    print(Solution().jump(nums))
