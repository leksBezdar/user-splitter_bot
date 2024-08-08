from dataclasses import dataclass

from src.domain.entities.users import UserEntity
from src.domain.services.users import IUserService
from src.gateways.postgresql.models.users import UserModel
from src.gateways.postgresql.repositories.users import IUserRepository


@dataclass
class ORMUserService(IUserService):
    repository: IUserRepository

    async def get_or_create(self, user: UserEntity) -> UserEntity:
        user_dto = await self.repository.get_or_create(UserModel.from_entity(user))
        return user_dto.to_entity()
