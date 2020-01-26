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
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_temp = []
        for i in range(len(nums)):
            temp_list = [0 for _ in range(len(nums))]
            for j in range(len(temp_list)):
                if i == j:
                    temp_list[j] = float('inf')
                    continue
                # b = -c -a
                temp_list[j] = -nums[i] - nums[j]
            for j in range(len(nums)):
                for k in range(len(temp_list)):
                    if nums[j] == temp_list[k] and j != k and i != k and i != j:
                        temp_res = [nums[i], nums[j], nums[k]]
                        temp_res.sort()
                        res_temp.append(temp_res)
        res = []
        for each in res_temp:
            if each not in res:
                res.append(each)
        return res

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:  # 排好序之后，如果nums[i]>0，说明后面的数全部大于0
                break
            if i == 0 or nums[i] > nums[i - 1]:  # 去重
                left, right = i + 1, len(nums) - 1
                # 剪枝，两种边界条件，b值已经足够大，即使是b和b的下一位相加都大于0 和c已经足够小，c和c的前一位相加已经小于0
                if nums[i] + nums[left] + nums[left + 1] > 0 or nums[i] + nums[right - 1] + nums[right] < 0:
                    continue
                while left < right:
                    ident = nums[i] + nums[left] + nums[right]
                    if ident == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 去重，将与当前结果一样的数字利用指针直接筛掉
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum1(nums))
