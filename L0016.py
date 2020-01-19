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
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dis = float('inf')
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if abs(nums[i] + nums[left] + nums[right] - target) < dis:
                    dis = abs(nums[i] + nums[left] + nums[right] - target)
                    res = [nums[i], nums[left], nums[right]]
                    # 判断指针移动方向
                if nums[i] + nums[left] + nums[right] - target < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] - target > 0:
                    right -= 1
                else:
                    return target
        return sum(res)


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    target = 82
    print(Solution().threeSumClosest(nums, target))
