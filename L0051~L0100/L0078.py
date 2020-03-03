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
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def back(res=[]):
            res_list.append(res[:])
            for i in range(len(nums)):
                if init_list[i] == 0:
                    init_list[i] = 1
                    if len(res) == 0 or res[-1] < nums[i]:
                        res.append(nums[i])
                        back(res[:])
                        res = res[:-1]
                    init_list[i] = 0

            pass

        init_list = [0 for _ in range(len(nums))]
        res_list = []
        back()
        return res_list
        pass


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))

