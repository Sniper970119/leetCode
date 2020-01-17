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
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        res = ''
        min_len = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        i = 0
        while True:
            if i < min_len:
                temp_str = strs[0][i]
            else:
                return res
            temp_flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != temp_str:
                    temp_flag = False
            if temp_flag == False:
                return res
            else:
                res += temp_str
                i += 1
        pass

    def longestCommonPrefix1(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

if __name__ == '__main__':
    strs = ["cc", 'ccc']
    print(Solution().longestCommonPrefix(strs))
