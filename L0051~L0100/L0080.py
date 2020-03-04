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
    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        flag_nub = nums[0]
        flag_times = 0
        current_idx = 0
        while len(nums) > 0:
            if current_idx == len(nums):
                return len(nums)
            if flag_nub == nums[current_idx] and flag_times < 2:
                flag_times += 1
            elif flag_nub == nums[current_idx]:
                nums.remove(nums[current_idx])
                current_idx -= 1
            else:
                flag_times = 1
                flag_nub = nums[current_idx]
            current_idx += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().removeDuplicates(nums))
