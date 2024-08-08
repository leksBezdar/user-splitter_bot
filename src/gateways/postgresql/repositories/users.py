from dataclasses import dataclass

from sqlalchemy import select

from gateways.postgresql.repositories.base import IUserRepository
from src.gateways.postgresql.database import Database
from src.gateways.postgresql.models.users import UserModel


@dataclass
class ORMUserRepository(IUserRepository):
    database: Database

    async def create(self, user: UserModel) -> UserModel:
        async with self.database.get_session() as session:
            session.add(user)
        return user

    async def get_or_create(self, user: UserModel) -> UserModel:
        db_user = await self.get_by_telegram_id(user.telegram_id)
        return db_user or await self.create(user)

    async def get_by_telegram_id(self, telegram_id: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.telegram_id == telegram_id).limit(1)
        async with self.database.get_read_only_session() as session:
            return await session.scalar(stmt)
