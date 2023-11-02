from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from core.data_models.user_data import UserData
from core.database.models.interfaces.user_model_interface import UserModelInterface
from core.database.session import get_db_session
from core.utils.password_hash import PasswordHasher

from auth.views.handlers.user_handler import UserHandler, UserHandlerMaker


auth_router = APIRouter()


@cbv(auth_router)
class Register:
    user_handler: UserHandler = Depends(
        UserHandlerMaker(
            interface=UserModelInterface(session_maker=get_db_session()),
            hasher=PasswordHasher()
        )
    )

    @auth_router.post("/register")
    async def register(self, user: UserData):
        await self.user_handler.add_user(user)

        return {"response": "OK"}
