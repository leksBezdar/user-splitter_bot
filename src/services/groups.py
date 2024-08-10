from dataclasses import dataclass

from src.domain.entities.groups import GroupEntity
from src.domain.services.groups import IGroupService
from src.gateways.postgresql.repositories.groups import IGroupRepository


@dataclass
class ORMGroupService(IGroupService):
    repository: IGroupRepository

    async def get_all(self, limit: int = 3, offset: int = 0) -> list[GroupEntity]:
        groups_dto = await self.repository.get_all(limit=limit, offset=offset)
        return [group_dto.to_entity() for group_dto in groups_dto]
