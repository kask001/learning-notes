#!/usr/bin/env python3
"""
冒泡排序 - 双向优化版 (Cocktail Shaker Sort)

在传统冒泡排序基础上，交替从左到右和从右到左遍历，
减少排序所需的趟数，对部分有序的数据更高效。
"""

from typing import List
import time


def cocktail_sort(arr: List[int]) -> List[int]:
    """
    实现双向冒泡排序（鸡尾酒排序）。

    Args:
        arr: 待排序的整数列表

    Returns:
        排序后的新列表
    """
    result = arr.copy()
    n = len(result)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False
        # 从左到右，将最大值冒泡到末尾
        for i in range(start, end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
        end -= 1

        # 从右到左，将最小值冒泡到开头
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        start += 1

    return result


if __name__ == "__main__":
    # 性能对比测试
    data = [random.randint(1, 1000) for _ in range(500)]
    print(f"鸡尾酒排序: {cocktail_sort(data[:10])}")

    # 基本测试
    print(f"基本测试: {cocktail_sort([5, 1, 4, 2, 8])}")
    print(f"逆序测试: {cocktail_sort([9, 7, 5, 3, 1])}")
