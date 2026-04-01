#!/usr/bin/env python3
"""
CSV 数据处理工具

使用 Python 内置 csv 模块读写 CSV 文件，
支持字典模式和列表模式。
"""

import csv
from typing import List, Dict, Any
from io import StringIO


def read_csv_string(csv_text: str) -> List[Dict[str, str]]:
    """
    从字符串读取 CSV 数据为字典列表。

    Args:
        csv_text: CSV 格式的字符串

    Returns:
        字典列表，每行一个字典
    """
    reader = csv.DictReader(StringIO(csv_text))
    return list(reader)


def write_csv_string(data: List[Dict[str, Any]]) -> str:
    """
    将字典列表转换为 CSV 字符串。

    Args:
        data: 字典列表

    Returns:
        CSV 格式的字符串
    """
    if not data:
        return ""
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def filter_csv(data: List[Dict[str, str]], column: str, value: str) -> List[Dict[str, str]]:
    """
    按列值过滤 CSV 数据。

    Args:
        data: CSV 字典列表
        column: 列名
        value: 要匹配的值

    Returns:
        过滤后的字典列表
    """
    return [row for row in data if row.get(column) == value]


def sort_csv(data: List[Dict[str, str]], column: str, reverse: bool = False) -> List[Dict[str, str]]:
    """
    按列值排序 CSV 数据。

    Args:
        data: CSV 字典列表
        column: 排序列名
        reverse: 是否降序

    Returns:
        排序后的字典列表
    """
    return sorted(data, key=lambda row: row.get(column, ""), reverse=reverse)


if __name__ == "__main__":
    csv_data = """name,age,city
Alice,30,Beijing
Bob,25,Shanghai
Charlie,35,Beijing
Diana,28,Guangzhou"""

    rows = read_csv_string(csv_data)
    print("原始数据:")
    for row in rows:
        print(f"  {row}")

    beijing = filter_csv(rows, "city", "Beijing")
    print(f"\n北京: {beijing}")

    sorted_rows = sort_csv(rows, "age")
    print(f"\n按年龄排序:")
    for row in sorted_rows:
        print(f"  {row['name']}: {row['age']}")
