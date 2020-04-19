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
from collections import Counter, defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points_dict = Counter(tuple(point) for point in points)
        not_repeat_point = list(points_dict.keys())
        if len(not_repeat_point) == 1:
            return points_dict[not_repeat_point[0]]
        if len(not_repeat_point) == 0:
            return 0
        res = 0
        for i in range(len(not_repeat_point) - 1):
            x1, y1 = not_repeat_point[i][0], not_repeat_point[i][1]
            k = defaultdict(int)
            for j in range(i + 1, len(not_repeat_point)):
                x2, y2 = not_repeat_point[j][0], not_repeat_point[j][1]
                dy, dx = y2 - y1, x2 - x1
                if dx == 0:
                    tmp = '#'
                    # continue
                else:
                    tmp = dy * 1000 / dx * 1000
                k[tmp] += points_dict[not_repeat_point[j]]
                pass
            res = max(res, max(k.values()) + points_dict[not_repeat_point[i]])
        return res


if __name__ == '__main__':
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    points = [[0, 0], [0, 1]]
    points = [[560, 248], [0, 16], [30, 250], [950, 187], [630, 277], [950, 187], [-212, -268], [-287, -222], [53, 37],
              [-280, -100], [-1, -14], [-5, 4], [-35, -387], [-95, 11], [-70, -13], [-700, -274], [-95, 11], [-2, -33],
              [3, 62], [-4, -47], [106, 98], [-7, -65], [-8, -71], [-8, -147], [5, 5], [-5, -90], [-420, -158],
              [-420, -158], [-350, -129], [-475, -53], [-4, -47], [-380, -37], [0, -24], [35, 299], [-8, -71], [-2, -6],
              [8, 25], [6, 13], [-106, -146], [53, 37], [-7, -128], [-5, -1], [-318, -390], [-15, -191], [-665, -85],
              [318, 342], [7, 138], [-570, -69], [-9, -4], [0, -9], [1, -7], [-51, 23], [4, 1], [-7, 5], [-280, -100],
              [700, 306], [0, -23], [-7, -4], [-246, -184], [350, 161], [-424, -512], [35, 299], [0, -24], [-140, -42],
              [-760, -101], [-9, -9], [140, 74], [-285, -21], [-350, -129], [-6, 9], [-630, -245], [700, 306], [1, -17],
              [0, 16], [-70, -13], [1, 24], [-328, -260], [-34, 26], [7, -5], [-371, -451], [-570, -69], [0, 27],
              [-7, -65], [-9, -166], [-475, -53], [-68, 20], [210, 103], [700, 306], [7, -6], [-3, -52], [-106, -146],
              [560, 248], [10, 6], [6, 119], [0, 2], [-41, 6], [7, 19], [30, 250]]
    print(Solution().maxPoints(points))
