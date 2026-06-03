#!/usr/bin/env python3
"""
Python 生成器 (Generators)

生成器是一种特殊的迭代器，使用 yield 关键字逐个产生值，
而不是一次性返回所有结果。适用于处理大数据集或无限序列。
"""

from typing import Generator, Iterable


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """生成斐波那契数列，直到超过 limit。"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def flatten(nested: Iterable) -> Generator:
    """递归展平嵌套的可迭代对象。"""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def read_file_in_chunks(filepath: str, chunk_size: int = 1024) -> Generator[str, None, None]:
    """
    按块读取文件，避免一次性加载大文件到内存。

    Args:
        filepath: 文件路径
        chunk_size: 每块的字符数
    """
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def batch_processor(items: list, batch_size: int) -> Generator[list, None, None]:
    """将列表分成指定大小的批次。"""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


if __name__ == "__main__":
    print(f"斐波那契 (<100): {list(fibonacci_generator(100))}")

    nested = [1, [2, [3, 4], 5], [6, [7, [8]]]]
    print(f"展平嵌套: {list(flatten(nested))}")

    items = list(range(1, 11))
    for i, batch in enumerate(batch_processor(items, 3)):
        print(f"批次 {i + 1}: {batch}")
