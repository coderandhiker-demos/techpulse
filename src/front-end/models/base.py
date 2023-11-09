from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase

class Base(MappedAsDataclass, DeclarativeBase):
    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }