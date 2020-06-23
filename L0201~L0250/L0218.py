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

import heapq


class Solution:
    def getSkyline(self, buildings):
        # 思路：最大堆，每次在判断关键点的时候，移除所有右端点≤当前点的堆顶。
        if not buildings: return []
        points = []
        heap = [[0, float('inf')]]
        res = [[0, 0]]
        res1 = []
        # 1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r))  # 这里负号将最小堆，变成了最大堆
            points.append((r, h, 0))  # r的右端点为0

        # 2.将端点从小到大排序
        points.sort()  # 如果当前点相等，则按照高度升序

        # 3.遍历每一个点，分别判断出堆、入堆、添加关键点操作。
        for l, h, r in points:
            while l >= heap[0][1]:  # 出堆：保证当前堆顶为去除之前建筑物右端点的最大值。
                heapq.heappop(heap)
            if h < 0:  # 入堆：所有左端点都要入堆
                heapq.heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]:  # 关键点：必然是左端点，堆顶，因此需要加负号
                res.append([l, -heap[0][0]])
            else:
                res1.append([l, -heap[0][0]])
        return res[1:]


if __name__ == '__main__':
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(Solution().getSkyline(buildings))
