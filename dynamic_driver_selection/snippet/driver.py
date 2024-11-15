import importlib.metadata
from abc import ABCMeta
from typing import Type, TypeVar

T = TypeVar("T")


class DriverType(ABCMeta):
    """Must be used as metaclass by classes defining a type of driver.

    This will provide a create(impl_name) class method to the new DriverType,
    enabling to load arbitrary implementation of the driver, from entry_point
    named DriverType.driver_entry_point_group.
    """

    driver_entry_point_group: str

    def __new__(cls, name, bases, attrs):
        try:
            attrs["driver_entry_point_group"]
        except KeyError:
            raise TypeError("Missing driver_entry_point_group on DriverType %s" % name)
        attrs["create"] = classmethod(cls.create)
        stuff = type(name, bases, attrs)
        return stuff

    def create(cls: Type[T], impl_name: str) -> T:
        """Create a new instance of specified type implementation."""
        try:
            entry_points = importlib.metadata.entry_points(
                group=cls.driver_entry_point_group, name=impl_name
            )
            entry_point = next(iter(entry_points))
            driver_cls = entry_point.load()
        except StopIteration:
            raise ValueError(
                "Driver of type %s has no registered implementation named: %s"
                % (cls.__name__, impl_name)
            )
        return driver_cls()
