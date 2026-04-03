#!/usr/bin/env python3
"""
归并排序 (Merge Sort)

经典的分治排序算法，递归地将数组分成两半，
分别排序后再合并。时间复杂度: O(n log n)，稳定排序。
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    实现归并排序。

    Args:
        arr: 待排序的列表

    Returns:
        排序后的新列表
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    合并两个已排序列表。

    Args:
        left: 已排序列表 1
        right: 已排序列表 2

    Returns:
        合并后的有序列表
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"排序前: {data}")
    print(f"排序后: {merge_sort(data)}")
    print(f"逆序: {merge_sort([5, 4, 3, 2, 1])}")
    print(f"重复元素: {merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5])}")
