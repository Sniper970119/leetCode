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
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def find(temp_nums):
            if len(temp_nums) == 0:
                return 0
            if len(temp_nums) == 1:
                return temp_nums[0]
            dp = [0 for _ in range(len(temp_nums))]
            dp[0] = temp_nums[0]
            dp[1] = max(temp_nums[0], temp_nums[1])
            for i in range(2, len(dp)):
                dp[i] = max(temp_nums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        return max(find(nums[0:-1]), find(nums[1:]))


if __name__ == '__main__':
    nums = [0, 0]
    print(Solution().rob(nums))
