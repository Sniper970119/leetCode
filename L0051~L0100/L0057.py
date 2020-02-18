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
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        def cmp(x, y):
            if x[0] > y[0]:
                return 1
            elif x[0] < y[0]:
                return -1
            else:
                return 0

        if len(intervals) == 0:
            return [newInterval]
        import functools
        intervals.append(newInterval)
        intervals = sorted(intervals, key=functools.cmp_to_key(cmp))
        do_length = 0
        do_idx = 1
        max_length = len(intervals)
        while do_length < max_length - 1:
            if intervals[do_idx][0] <= intervals[do_idx - 1][1]:
                intervals[do_idx - 1][1] = max(intervals[do_idx][1], intervals[do_idx - 1][1])
                intervals.remove(intervals[do_idx])
            else:
                do_idx += 1
            do_length += 1
        return intervals


if __name__ == '__main__':
    intervals = []
    newInterval = [5, 7]
    print(Solution().insert(intervals, newInterval))
