#!/usr/bin/env python3
"""
日志配置工具

封装 Python logging 模块的常用配置，
支持控制台和文件输出，按日期轮转日志文件。
"""

import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str,
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    fmt: Optional[str] = None,
) -> logging.Logger:
    """
    创建并配置一个 logger。

    Args:
        name: logger 名称
        level: 日志级别
        log_file: 日志文件路径（可选）
        fmt: 日志格式字符串（可选）

    Returns:
        配置好的 Logger 实例
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 防止重复添加 handler
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt or "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 控制台 handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 文件 handler（如果指定了日志文件）
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# 使用示例
if __name__ == "__main__":
    app_logger = setup_logger("myapp", log_file="logs/app.log")

    app_logger.debug("这是一条调试信息")
    app_logger.info("应用启动成功")
    app_logger.warning("磁盘空间不足")
    app_logger.error("数据库连接失败")

    # 不同模块的 logger
    db_logger = setup_logger("myapp.database")
    db_logger.info("数据库连接池初始化完成")

    api_logger = setup_logger("myapp.api")
    api_logger.info("API 服务启动在端口 8080")
