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
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def find_max(m, n):
            """寻找最大值"""
            if m >= n:
                return m
            mid = (m + n) // 2
            if nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] >= nums[0]:
                return find_max(mid + 1, n)
            else:
                return find_max(m, mid - 1)

        def binary_search(m, n):
            """
            二分查找
            :param m:
            :param n:
            :return:
            """
            if m > n:
                return -1
            mid = (m + n) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, n)
            else:
                return binary_search(m, mid - 1)

        max_idx = find_max(0, len(nums) - 1)
        return binary_search(0, max_idx) if binary_search(0, max_idx) != -1 else binary_search(max_idx + 1,
                                                                                               len(nums) - 1)


if __name__ == '__main__':
    nums = [8, 9, 2, 3, 4]
    print(Solution().search(nums, 9))
