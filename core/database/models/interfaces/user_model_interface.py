from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from core.data_models.user_data import UserData
from core.database.models.user_model import User
from core.utils.password_hash import PasswordHasher


class UserModelInterface:
    def __init__(self, session_maker: sessionmaker):
        self.model = User
        self.session_maker = session_maker

    def add_user(self, data: UserData, hasher: PasswordHasher):
        with self.session_maker() as session:
            hash, salt = hasher.hash(data.password)

            user = self.model(
                username=data.username,
                hashed_password=hash,
                salt=salt,
                email=data.email
            )

            session.add(user)
            session.commit()

    def get_user(self, data: UserData):
        with self.session_maker() as session:
            user = session.execute(
                select(self.model)
                .where(self.model.username == data.username)
                .where(self.model.email == data.email)
            ).one_or_none()

            return user

