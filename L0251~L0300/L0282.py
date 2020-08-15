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
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res_list = []
        operator_list = ['+', '-', '*', '']

        def back(cur_str, sub_num):
            if sub_num == '':
                try:
                    if eval(cur_str) == target:
                        res_list.append(cur_str)
                except:
                    pass
                return
            for each in operator_list:
                # if each == '' and cur_str[-1] == '0':
                #     continue
                cur_str = cur_str + str(each) + sub_num[:1]
                back(cur_str, sub_num[1:])
                cur_str = cur_str[:-2]

        back(num[:1], num[1:])
        return res_list


if __name__ == '__main__':
    num = '1000000009'
    target = 9
    # num = '000'
    # target = 0
    print(Solution().addOperators(num, target))
