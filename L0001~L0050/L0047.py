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

    def permuteUnique1(self, nums):
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
        output_final = []

        backtrack(0, flag_list)
        for each in output:
            if each not in output_final:
                output_final.append(each)
        return output_final


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique1(nums))
