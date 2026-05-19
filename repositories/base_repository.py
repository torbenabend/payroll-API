from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic, Optional, List

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):
    model: Type[T]
    schema: Type[T]

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> T:
        pass

    @abstractmethod
    def get_entities(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass
