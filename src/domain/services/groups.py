from abc import ABC, abstractmethod

from src.domain.entities.groups import GroupEntity


class IGroupService(ABC):
    @abstractmethod
    async def get_all(self, limit: int = 3, offset: int = 9) -> GroupEntity:
        pass
