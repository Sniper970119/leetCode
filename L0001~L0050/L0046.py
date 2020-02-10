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
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # 这里使用交换来模拟递归其余数字（比如1,2,3。 交换1 2   13  就模拟了第一个位置的全部可能）
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

    def permute1(self, nums):
        def backtrack(i, flag_list, temp_list=[]):
            if i == n:
                output.append(temp_list)
                return
            # 找到第一个可用数字
            for j in range(len(flag_list)):
                if flag_list[j] != 0:
                    flag_list[j] = 0
                    temp_list.append(nums[j])
                    backtrack(i + 1, flag_list[:], temp_list[:])
                    flag_list[j] = 1
                    temp_list = temp_list[:-1]

        n = len(nums)
        output = []
        flag_list = [1 for _ in range(n)]
        backtrack(0, flag_list)
        return output


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute1(nums))
