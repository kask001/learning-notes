#!/usr/bin/env python3
"""
策略模式 (Strategy Pattern)

定义一系列算法，将每个算法封装起来，使它们可以互换。
让算法的变化独立于使用它的客户端。

示例：实现多种折扣策略，用于电商结算。
"""

from abc import ABC, abstractmethod
from typing import List


# 策略接口
class DiscountStrategy(ABC):
    """折扣策略抽象基类。"""

    @abstractmethod
    def calculate(self, total: float) -> float:
        """计算折后价格。"""
        pass


# 具体策略
class NoDiscount(DiscountStrategy):
    """无折扣。"""

    def calculate(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    """百分比折扣。"""

    def __init__(self, percent: float):
        self.percent = percent

    def calculate(self, total: float) -> float:
        return total * (1 - self.percent / 100)


class FixedDiscount(DiscountStrategy):
    """固定金额折扣（满减）。"""

    def __init__(self, threshold: float, discount: float):
        self.threshold = threshold
        self.discount = discount

    def calculate(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.discount
        return total


# 上下文
class ShoppingCart:
    """购物车。"""

    def __init__(self):
        self.items: List[tuple] = []
        self._strategy: DiscountStrategy = NoDiscount()

    def add_item(self, name: str, price: float):
        self.items.append((name, price))

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def get_total(self) -> float:
        subtotal = sum(price for _, price in self.items)
        return self._strategy.calculate(subtotal)


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Python编程书", 89.0)
    cart.add_item("机械键盘", 399.0)
    cart.add_item("显示器", 1999.0)

    print(f"原价: ¥{cart.get_total():.2f}")

    cart.set_discount_strategy(PercentageDiscount(10))
    print(f"九折: ¥{cart.get_total():.2f}")

    cart.set_discount_strategy(FixedDiscount(threshold=2000, discount=200))
    print(f"满2000减200: ¥{cart.get_total():.2f}")
