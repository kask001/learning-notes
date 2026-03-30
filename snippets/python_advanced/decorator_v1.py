#!/usr/bin/env python3
"""
Python 装饰器 (Decorators)

装饰器是 Python 中强大的语法特性，用于在不修改函数源代码的情况下
扩展函数的功能。本质是高阶函数，接受一个函数并返回一个新函数。
"""

import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """计时装饰器：测量函数执行时间。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[计时] {func.__name__} 执行耗时: {elapsed:.4f}秒")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """重试装饰器：失败时自动重试。"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"[重试] 第 {attempt} 次失败: {e}，{delay}秒后重试...")
                    time.sleep(delay)
        return wrapper
    return decorator


def validate_positive(func: Callable) -> Callable:
    """参数校验装饰器：确保所有参数为正数。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"参数必须为正数，收到: {arg}")
        return func(*args, **kwargs)
    return wrapper


@timer
def slow_function(n: int) -> int:
    """模拟耗时操作。"""
    total = sum(i * i for i in range(n))
    return total


@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    """模拟不稳定操作。"""
    import random
    if random.random() < 0.5:
        raise ConnectionError("连接失败")
    return "成功!"


@validate_positive
def calculate_area(radius: float) -> float:
    """计算圆面积。"""
    import math
    return math.pi * radius * radius


if __name__ == "__main__":
    slow_function(100000)

    result = unreliable_function()
    print(f"不稳定操作结果: {result}")

    print(f"面积: {calculate_area(5):.2f}")
