from dataclasses import dataclass

from sqlalchemy import select

from gateways.postgresql.repositories.base import IGroupRepository
from src.gateways.postgresql.database import Database
from src.gateways.postgresql.models.groups import GroupModel


@dataclass
class ORMGroupRepository(IGroupRepository):
    database: Database

    async def get_all(self, limit: int = 3, offset: int = 0) -> list[GroupModel]:
        stmt = select(GroupModel).limit(limit).offset(offset)
        async with self.database.get_read_only_session() as session:
            result = await session.execute(stmt)
            return result.scalars().all()
