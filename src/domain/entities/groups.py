from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

from domain.entities.users import UserEntity


@dataclass
class GroupEntity:
    group_oid: UUID = field(default_factory=uuid4)
    name: str
    description: str | None = None
    users: list[UserEntity] = field(default_factory=list)
    interests: list[str | None] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    max_members_number: int = field(init=False)

    def __post_init__(self):
        self.max_members_number = 20

    @property
    def members_number(self) -> int:
        return len(self.users)

    def add_user(self, user: UserEntity) -> None:
        """Добавление пользователя в группу, если есть свободное место."""
        if self.members_number < self.max_members_number:
            self.users.append(user)
        else:
            raise ValueError("Группа достигла максимального числа участников")

    def remove_user(self, user: UserEntity) -> None:
        """Удаление пользователя из группы."""
        if user in self.users:
            self.users.remove(user)
