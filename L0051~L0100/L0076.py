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
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        weight_list = []
        str_list = []
        temp_weight = 0
        for i in range(len(s)):
            if s[i] not in t:
                temp_weight += 1
                continue
            temp_weight += 1
            str_list.append(s[i])
            weight_list.append(temp_weight)
            temp_weight = 0
        windows_length = len(t)
        current_min_idx = -1
        current_min_val = float('inf')
        for i in range(len(str_list) - windows_length + 1):
            queue = []
            temp_val = 0
            for j in range(windows_length):
                if len(queue) != len(t) and str_list[i + j] not in queue:
                    queue.append(str_list[i + j])
                    if j != 0:
                        temp_val += weight_list[i + j]
                    else:
                        temp_val += 1
                if len(queue) == len(t):
                    if temp_val < current_min_val:
                        current_min_idx = i
                        current_min_val = temp_val
        if current_min_idx == -1:
            return ''
        from_idx = 0
        for i in range(current_min_idx + 1):
            from_idx += weight_list[i]
        return s[from_idx - 1:from_idx + current_min_val - 1]


if __name__ == '__main__':
    S = "aa"
    T = "aa"
    # S = "ADOBECODEBANC"
    # T = "ABC"
    print(Solution().minWindow(S, T))
