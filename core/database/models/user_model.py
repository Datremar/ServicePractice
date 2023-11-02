from sqlalchemy import Column, Integer, String, Boolean

from database.base import Base
from database.engine import engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    salt = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
