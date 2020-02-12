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
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 1:
            return [strs]
        temp_strs = strs[:]
        for i in range(len(strs)):
            strs[i] = "".join((lambda x: (x.sort(), x)[1])(list(strs[i])))
        # 保存结果
        res_strs = []
        # 保存已经有了的排序后的字符串
        temp_list = []
        for i in range(len(strs)):
            if strs[i] in temp_list:
                idx = temp_list.index(strs[i])
                res_strs[idx].append(temp_strs[i])
            else:
                res_strs.append([temp_strs[i]])
                temp_list.append(strs[i])
        return res_strs


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
