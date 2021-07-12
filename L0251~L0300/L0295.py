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
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_list = []
        self.min_list = []
        heapq.heapify(self.max_list)
        heapq.heapify(self.min_list)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_list, num)
        heapq.heappush(self.max_list, -heapq.heappop(self.min_list))
        if len(self.min_list) < len(self.max_list):
            heapq.heappush(self.min_list, -heapq.heappop(self.max_list))

    def findMedian(self) -> float:
        if len(self.min_list) != len(self.max_list):
            return self.min_list[0]
        else:
            return (-self.max_list[0] + self.min_list[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
