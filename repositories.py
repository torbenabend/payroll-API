from database import Session
from models import Role


class BaseRepository:
    def __init__(self):
        self.session = Session()

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()
        return obj

    def get_by_id(self, obj_id):
        return self.session.get(self.model, obj_id)

    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()
        return obj

    def get_objects(self):
        return self.session.query(self.model).all()

    def update(self, obj):
        self.session.commit()
        return obj



class RoleRepository(BaseRepository):
    model = Role

    def create_role(self, new_role: Role) -> Role:
        return self.add(new_role)


    def delete_role(self, role_to_delete: Role) -> Role:
        pass
