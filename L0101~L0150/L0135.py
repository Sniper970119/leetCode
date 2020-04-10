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
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        pre_order = [1]
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                pre_order.append(pre_order[-1] + 1)
            else:
                pre_order.append(1)
        back_order = [1]
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                back_order.insert(0, back_order[0] + 1)
            else:
                back_order.insert(0, 1)
        res = []
        for i in range(len(ratings)):
            res.append(max(pre_order[i], back_order[i]))
        return sum(res)
        pass


if __name__ == '__main__':
    ratings = [1, 0, 2]
    print(Solution().candy(ratings))
