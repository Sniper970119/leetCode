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
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        from_idx = -float('inf')
        to_idx = -float('inf')
        res_list = []
        nums.append(-float('inf'))
        for each in nums:
            if from_idx == -float('inf'):
                from_idx = each
                to_idx = from_idx
                continue
            if each == to_idx + 1:
                to_idx += 1
            else:
                if to_idx - from_idx == 0:
                    res_list.append(str(to_idx))
                    from_idx = to_idx = each
                else:
                    res_list.append(str(from_idx) + '->' + str(to_idx))
                    from_idx = to_idx = each
        return res_list


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    nums = [0, 2, 3, 4, 6, 8, 9]
    # nums = [-1]
    print(Solution().summaryRanges(nums))
