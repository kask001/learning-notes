#!/usr/bin/env python3
"""
上下文管理器 (Context Managers)

使用 with 语句管理资源的获取和释放。
确保资源在使用后被正确清理，即使发生异常。

两种实现方式：
1. 类实现 __enter__ 和 __exit__
2. 使用 contextlib.contextmanager 装饰器
"""

import time
from contextlib import contextmanager


# 方式 1: 基于类的上下文管理器
class Timer:
    """计时上下文管理器。"""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"耗时: {self.elapsed:.4f}秒")
        return False  # 不吞掉异常


class FileProcessor:
    """安全的文件处理上下文管理器。"""

    def __init__(self, filepath: str, mode: str = "r"):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"文件操作出错: {exc_val}")
        return False


# 方式 2: 基于生成器的上下文管理器
@contextmanager
def database_connection(db_url: str):
    """模拟数据库连接上下文。"""
    print(f"连接数据库: {db_url}")
    conn = {"connected": True, "url": db_url}
    try:
        yield conn
    finally:
        conn["connected"] = False
        print("数据库连接已关闭")


@contextmanager
def suppress_errors(*error_types):
    """抑制指定类型的错误。"""
    try:
        yield
    except error_types as e:
        print(f"[抑制错误] {type(e).__name__}: {e}")


if __name__ == "__main__":
    with Timer():
        total = sum(i**2 for i in range(100000))

    with database_connection("postgresql://localhost/mydb") as conn:
        print(f"连接状态: {conn['connected']}")

    with suppress_errors(ZeroDivisionError, ValueError):
        result = 10 / 0
        print("这行不会执行")
    print("继续执行...")
