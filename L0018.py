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
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        # 选定a
        for i in range(len(nums)):
            # 选定b
            if i > 0 and nums[i] == nums[i- 1]:
                continue
            new_target = target - nums[i]
            new_nums = nums[i + 1:]
            for j in range(len(new_nums) - 2):
                left = j + 1
                right = len(new_nums) - 1
                if j > 0 and new_nums[j] == new_nums[j - 1]:
                    continue
                while left < right:
                    temp = new_nums[j] + new_nums[left] + new_nums[right]
                    if temp == new_target:
                        res_list = [nums[i], new_nums[j], new_nums[left], new_nums[right]]
                        res_list.sort()
                        res.append(res_list)
                        left += 1
                        right -= 1
                        # 初步去重（相当于剪枝？）
                        while left < right and new_nums[left] == new_nums[left - 1]:
                            left += 1
                        while left < right and new_nums[right] == new_nums[right + 1]:
                            right -= 1
                    if temp > new_target:
                        right -= 1
                    if temp < new_target:
                        left += 1
        # 最后硬核去重
        res_final = []
        for each in res:
            if each not in res_final:
                res_final.append(each)
        return res_final


if __name__ == '__main__':
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    print(Solution().fourSum(nums, target))
