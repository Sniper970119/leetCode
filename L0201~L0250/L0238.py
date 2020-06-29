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
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        ans1 = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            ans1[i] = ans1[i - 1] * nums[i - 1]
        ans2 = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            ans2[i] = ans2[i + 1] * nums[i + 1]
        ans = []
        for i in range(len(nums)):
            ans.append(ans1[i] * ans2[i])
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))

    # 1 1 2 6
    # 24 12 4 1
# 24 12 8 6
