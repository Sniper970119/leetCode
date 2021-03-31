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
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛

"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [1 for _ in range(len(nums))]
        # res[0] = 1
        for i in range(1, len(nums)):
            tmp_max = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    tmp_max = max(tmp_max, res[j]+res[i])
            res[i] = tmp_max
        return max(res)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [7]
    #       1   1  1  2  2  3   4   4
    print(Solution().lengthOfLIS(nums))
    pass
