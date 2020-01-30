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


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)

        def reverse(nums, i, j):
            """
            翻转列表
            :param nums:
            :param i:
            :param j:
            :return:
            """
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # 正序查找
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        # 查找不到直接翻转返回
        if firstIndex == -1:
            reverse(nums, 0, n - 1)
            return nums
        # 翻转查找
        secondIndex = -1
        for i in range(n - 1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        # 交换两次查找的索引
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        # 翻转回来返回
        reverse(nums, firstIndex + 1, n - 1)
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().nextPermutation(nums))
