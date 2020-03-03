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
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def back(res=[]):
            if len(res) == k:
                res_list.append(res)
                return
            for i in range(n):
                if init_list[i] == 0:
                    init_list[i] = 1
                    if len(res) == 0 or res[-1] < i + 1:
                        res.append(i + 1)
                        back(res[:])
                        res = res[:-1]
                    init_list[i] = 0

            pass

        init_list = [0 for _ in range(n)]
        res_list = []
        back()
        return res_list


if __name__ == '__main__':
    n = 4
    k = 3
    print(Solution().combine(n, k))
