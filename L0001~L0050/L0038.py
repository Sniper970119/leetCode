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
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        pre_str = self.countAndSay(n - 1)
        res = ''
        count = 1
        temp_list = []
        for i in range(len(pre_str) - 1):
            if pre_str[i] == pre_str[i + 1]:
                count += 1
            else:
                temp_list.append(str(count) + pre_str[i])
                count = 1
        if count == 1:
            temp_list.append('1' + pre_str[-1])
        else:
            temp_list.append(str(count) + pre_str[-1])
        for i in range(len(temp_list)):
            res += temp_list[i]
        return res


if __name__ == '__main__':
    n = 5
    print(Solution().countAndSay(n))
