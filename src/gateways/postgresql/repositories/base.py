from abc import ABC, abstractmethod

from gateways.postgresql.models.groups import GroupModel
from gateways.postgresql.models.users import UserModel


class IUserRepository(ABC):
    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: str) -> UserModel | None:
        pass

    @abstractmethod
    async def create(self, user: UserModel) -> UserModel:
        pass

    @abstractmethod
    async def get_or_create(self, user: UserModel) -> UserModel:
        pass


class IGroupRepository(ABC):
    @abstractmethod
    async def get_all(self, limit: int = 3, offset: int = 0) -> list[GroupModel]:
        pass
