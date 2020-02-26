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
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        command = path.split('/')
        stack = []
        for each in command:
            if '.' == each:
                continue
            elif '..' == each:
                if len(stack) > 0:
                    stack.pop()
            elif '' == each:
                continue
            else:
                stack.append(each)
        res = ''
        if len(stack) == 0:
            return '/'
        for each in stack:
            res += str('/' + each)
        return res


if __name__ == '__main__':
    path = "/a/./b/../../c/"
    path = "/a//b////c/d//././/.."
    path = '/../'
    path = '/home/'
    print(Solution().simplifyPath(path))
