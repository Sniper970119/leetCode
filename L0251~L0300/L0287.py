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
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        fast = 0
        while res != fast or fast == 0:
            res = nums[res]
            fast = nums[nums[fast]]
            print()
        print(res)
        i = 0
        while res != i:
            res = nums[res]
            i = nums[i]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 2, 2]
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(Solution().findDuplicate(nums))
