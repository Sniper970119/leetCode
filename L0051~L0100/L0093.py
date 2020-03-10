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
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def find(idx, temp_list):
            if len(temp_list) > 4:
                return
            if len(temp_list) == 4 and idx == len(s):
                res.append('.'.join(temp_list))
                return
            for i in range(3):
                temp_s = s[idx:i + idx + 1]
                if temp_s == '' or str(int(temp_s)) != temp_s:
                    return
                if int(temp_s) < 256:
                    temp_list.append(temp_s)
                    find(idx + i + 1, temp_list[:])
                    temp_list = temp_list[:-1]
            pass

        res = []
        find(0, [])
        return res


if __name__ == '__main__':
    s = '25525511135'
    s = '010010'
    print(Solution().restoreIpAddresses(s))
