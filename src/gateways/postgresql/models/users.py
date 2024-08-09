import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gateways.postgresql.models.groups import GroupModel
from src.domain.entities.users import UserEntity
from src.gateways.postgresql.models.base import Base
from src.gateways.postgresql.models.mixins import UpdatedAtMixin, UUIDOidMixin


class UserModel(Base, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    telegram_id: Mapped[str] = mapped_column(sa.String(12), unique=True)
    first_name: Mapped[str | None] = mapped_column(sa.String(128))
    last_name: Mapped[str | None] = mapped_column(sa.String(128))
    username: Mapped[str | None] = mapped_column(sa.String(128))
    language_code: Mapped[str | None] = mapped_column(sa.String(8))

    groups: Mapped[list[GroupModel]] = relationship(
        "GroupModel", secondary="group_users", back_populates="users"
    )

    @staticmethod
    def from_entity(obj: UserEntity) -> "UserModel":
        return UserModel(
            telegram_id=obj.telegram_id,
            first_name=obj.first_name,
            last_name=obj.last_name,
            username=obj.username,
            language_code=obj.language_code,
        )

    def to_entity(self) -> UserEntity:
        return UserEntity(
            oid=self.oid,
            telegram_id=self.telegram_id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            language_code=self.language_code,
        )
