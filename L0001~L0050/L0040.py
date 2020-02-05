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
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            """
            回溯法
            :param i: 当前选择的索引
            :param tmp_sum: 当前已选择所有数的和
            :param tmp: 当前已选择数的列表
            :return:
            """
            if tmp_sum > target or i == n + 1:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j + 1, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])
        res_final = []
        # 去重
        for each in res:
            if each not in res_final:
                res_final.append(each)
        return res_final


if __name__ == '__main__':
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    # target = 8
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(Solution().combinationSum(candidates, target))
