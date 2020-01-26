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
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        res = ['()']
        for i in range(n - 1):
            temp_list = []
            for each in res:
                for j in range(len(each)):
                    temp_str = each[:j + 1] + '()' + each[j + 1:]
                    print(each, temp_str)
                    temp_list.append(temp_str)
            res = temp_list
        res_fin = []
        for each in res:
            if each not in res_fin:
                res_fin.append(each)
        return res_fin
        pass

    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        result = []
        for i in range(n):
            j = n - 1 - i
            temp1 = self.generateParenthesis(i)
            temp2 = self.generateParenthesis(j)
            result.extend(["(%s)%s" % (p, q) for p in temp1 for q in temp2])
        return result


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
