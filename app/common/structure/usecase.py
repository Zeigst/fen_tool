from abc import abstractmethod
from typing import Any

class BaseUseCase:
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise NotImplementedError()
