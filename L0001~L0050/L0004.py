# -*- coding:utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findKthElement(arr1, arr2, k):
            """
            寻找第k个元素
            :param nums1:
            :param nums2:
            :param k:
            :return:
            """
            l1, l2 = len(arr1), len(arr2)
            if l1 > l2:
                return findKthElement(arr2, arr1, k)
            if not arr1:
                return arr2[k - 1]
            if k == 1:
                return min(arr1[0], arr2[0])
            value1 = min(k // 2, l1) - 1
            value2 = min(k // 2, l2) - 1
            if arr1[value1] > arr2[value2]:
                return findKthElement(arr1, arr2[value2 + 1:], k - value2 - 1)
            else:
                return findKthElement(arr1[value1 + 1:], arr2, k - value1 - 1)

        ll1, ll2 = len(nums1), len(nums2)
        left, right = (ll1 + ll2 + 1) // 2, (ll1 + ll2 + 2) // 2
        return (findKthElement(nums1, nums2, left) + findKthElement(nums1, nums2, right)) / 2.0


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
