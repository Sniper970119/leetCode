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
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def get_num():
            res = num_list[-1]
            num_list.remove(res)
            return res


        num_list = [i for i in range(1, n * n + 1)]
        res_list = [[get_num()]]
        for i in range(2 * n - 2):
            temp_list = []
            # 加
            for j in range(len(res_list[0])):
                temp_list.insert(0, get_num())
            res_list.insert(0, temp_list)
            if len(num_list) == 0:
                return res_list
            # 翻
            temp_iter = res_list.__iter__()
            res_list = [i for i in zip(*temp_iter)]
            # 倒
            for j in range(len(res_list)):
                res_list[j] = res_list[j][::-1]
        return res_list


if __name__ == '__main__':
    n = 1
    print(Solution().generateMatrix(n))
