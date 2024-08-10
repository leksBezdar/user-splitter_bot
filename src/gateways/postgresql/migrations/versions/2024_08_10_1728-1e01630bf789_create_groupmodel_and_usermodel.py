"""Create GroupModel and UserModel

Revision ID: 1e01630bf789
Revises: 
Create Date: 2024-08-10 17:28:48.228286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e01630bf789'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('interests', sa.ARRAY(sa.String(length=20)), nullable=True),
    sa.Column('oid', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='Дата создания записи'),
    sa.PrimaryKeyConstraint('oid'),
    sa.UniqueConstraint('oid')
    )
    op.create_table('users',
    sa.Column('telegram_id', sa.String(length=12), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('language_code', sa.String(length=8), nullable=True),
    sa.Column('oid', sa.Uuid(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='Дата обновления записи'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='Дата создания записи'),
    sa.PrimaryKeyConstraint('oid'),
    sa.UniqueConstraint('oid'),
    sa.UniqueConstraint('telegram_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('groups')
    # ### end Alembic commands ###