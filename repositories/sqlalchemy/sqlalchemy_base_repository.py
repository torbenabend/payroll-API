from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository, T


class SqlAlchemyBaseRepository(BaseRepository[T]):
    def __init__(self, session: Session):
        self.session = session

    def add(self, entity: T) -> T:
        entity_db = self.model(**entity.model_dump())
        self.session.add(entity_db)
        self.session.commit()
        return self.schema.model_validate(entity_db)

    def get_by_id(self, entity_id: int) -> Optional[T]:
        entity_db = self.session.get(self.model, entity_id)
        if entity_db:
            return self.schema.model_validate(entity_db)
        return None

    def delete(self, entity_id: int) -> Optional[T]:
        entity_db = self.get_by_id(entity_id)
        if entity_db:
            self.session.delete(entity_db)
            self.session.commit()
            return self.schema.model_validate(entity_db)
        return None

    def get_entities(self) -> Optional[List[T]]:
        stmt = select(self.model)
        entities_db = self.session.execute(stmt).scalars().all()
        if entities_db:
            return [
                self.schema.model_validate(entity_db)
                for entity_db in entities_db
            ]
        return None

    def update(self, entity: T) -> T:
        update_data = entity.model_dump(exclude_unset=True)
        entity_db = self.session.get(self.model, entity.id)
        for column, value in update_data.items():
            setattr(entity_db, column, value)
        self.session.commit()
        return entity
