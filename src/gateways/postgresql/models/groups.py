import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.entities.groups import GroupEntity
from src.gateways.postgresql.models.base import Base
from src.gateways.postgresql.models.mixins import CreatedAtOnlyMixin, UUIDOidMixin


class GroupModel(Base, UUIDOidMixin, CreatedAtOnlyMixin):
    __table_args__ = {"extend_existing": True}

    name: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    description: Mapped[str | None] = mapped_column(sa.Text, nullable=True)
    interests: Mapped[list[str | None]] = mapped_column(
        sa.ARRAY(sa.String(20)), nullable=True
    )

    users = relationship("UserModel", back_populates="group")

    @staticmethod
    def from_entity(entity: GroupEntity) -> "GroupModel":
        return GroupModel(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            interests=entity.interests,
            created_at=entity.created_at,
        )

    def to_entity(self) -> GroupEntity:
        return GroupEntity(
            oid=self.oid,
            name=self.name,
            description=self.description,
            interests=self.interests,
            created_at=self.created_at,
        )
