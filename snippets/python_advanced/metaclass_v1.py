#!/usr/bin/env python3
"""
元类 (Metaclasses)

元类是类的类，控制类的创建过程。
Python 中 type 是默认的元类，我们可以自定义元类来
在类创建时自动添加属性、方法或进行验证。
"""


class ValidationError(Exception):
    """验证错误。"""
    pass


class ValidatedMeta(type):
    """
    验证元类：自动为类添加属性验证功能。
    会检查类属性是否为声明的类型。
    """

    def __new__(mcs, name, bases, namespace):
        # 收集字段类型声明
        field_types = {}
        for key, value in namespace.items():
            if isinstance(value, type):
                field_types[key] = value

        # 创建类
        cls = super().__new__(mcs, name, bases, namespace)
        cls._field_types = field_types

        # 如果有字段，添加 __init__
        if field_types:
            original_init = cls.__init__ if "__init__" in namespace else None

            def __init__(self, **kwargs):
                for field_name, field_type in self._field_types.items():
                    if field_name in kwargs:
                        value = kwargs[field_name]
                        if not isinstance(value, field_type):
                            raise ValidationError(
                                f"字段 '{field_name}' 期望 {field_type.__name__}，"
                                f"得到 {type(value).__name__}"
                            )
                        setattr(self, field_name, value)
                if original_init:
                    original_init(self, **kwargs)

            cls.__init__ = __init__

        return cls


class SingletonMeta(type):
    """单例元类实现。"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


if __name__ == "__main__":
    # 使用验证元类
    class User(metaclass=ValidatedMeta):
        name = str
        age = int
        email = str

        def __init__(self, **kwargs):
            pass

        def __repr__(self):
            return f"User(name={self.name!r}, age={self.age})"

    u = User(name="Alice", age=30, email="alice@example.com")
    print(u)

    try:
        User(name="Bob", age="invalid")  # 应该报错
    except ValidationError as e:
        print(f"验证错误: {e}")
