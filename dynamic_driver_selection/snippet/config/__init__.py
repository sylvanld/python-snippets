from abc import ABC, abstractmethod

from snippet.driver import DriverType


class Config(ABC, metaclass=DriverType):
    driver_entry_point_group = "snippet.config.driver"

    @abstractmethod
    def get(self, key: str):
        raise NotImplementedError
