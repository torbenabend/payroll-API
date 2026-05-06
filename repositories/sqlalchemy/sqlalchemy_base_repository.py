from typing import Optional, List
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository, T


class SqlAlchemyBaseRepository(BaseRepository[T]):
    def __init__(self, session: Session):
        self.session = session

    def add(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        return entity

    def get_by_id(self, entity_id: int) -> Optional[T]:
        return self.session.get(self.model, entity_id)

    def delete(self, entity: T) -> T:
        self.session.delete(entity)
        self.session.commit()
        return entity

    def get_entities(self) -> List[T]:
        return self.session.query(self.model).all()

    def update(self, entity: T) -> T:
        self.session.commit()
        return entity
