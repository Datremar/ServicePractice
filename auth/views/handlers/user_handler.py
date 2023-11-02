from core.data_models.user_data import UserData
from core.database.models.interfaces.user_model_interface import UserModelInterface
from core.utils.password_hash import PasswordHasher


class UserHandler:
    def __init__(self, interface: UserModelInterface, hasher: PasswordHasher):
        self.interface = interface
        self.hasher = hasher

    async def add_user(self, data: UserData):
        self.interface.add_user(data=data, hasher=self.hasher)


class UserHandlerMaker:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return UserHandler(*self.args, **self.kwargs)
