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
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        queue = []
        for i in range(len(tokens)):
            try:
                token_i = int(tokens[i])
                queue.append(token_i)
            except:
                handle_nub_1 = queue.pop()
                handle_nub_2 = queue.pop()
                if tokens[i] == '+':
                    queue.append(handle_nub_2 + handle_nub_1)
                elif tokens[i] == '-':
                    queue.append(handle_nub_2 - handle_nub_1)
                elif tokens[i] == '*':
                    queue.append(handle_nub_2 * handle_nub_1)
                else:
                    queue.append(int(handle_nub_2 / handle_nub_1))
                    pass
                pass
        return queue[0]
        pass


if __name__ == '__main__':
    tokens = ['2', '1', '+', '3', '*']
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
