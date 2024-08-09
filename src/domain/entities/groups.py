from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

from domain.entities.users import UserEntity


@dataclass
class GroupEntity:
    name: str
    description: str | None = None
    oid: UUID = field(default_factory=uuid4)
    users: list[UserEntity] = field(default_factory=list)
    interests: list[str | None] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def members_number(self) -> int:
        return len(self.users)

    def add_user(self, user: UserEntity) -> None:
        self.users.append(user)

    def remove_user(self, user: UserEntity) -> None:
        if user in self.users:
            self.users.remove(user)
