from abc import ABC, abstractmethod

from src.domain.entities.users import UserEntity


class IUserService(ABC):
    @abstractmethod
    async def get_or_create(self, user: UserEntity) -> UserEntity:
        pass
