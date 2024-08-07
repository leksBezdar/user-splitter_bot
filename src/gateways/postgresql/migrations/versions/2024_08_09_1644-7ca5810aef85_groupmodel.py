"""GroupModel

Revision ID: 7ca5810aef85
Revises: 6b08c223fa83
Create Date: 2024-08-09 16:44:16.695186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ca5810aef85'
down_revision: Union[str, None] = '6b08c223fa83'
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
    op.create_table('group_users',
    sa.Column('group_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.oid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.oid'], ),
    sa.PrimaryKeyConstraint('group_id', 'user_id')
    )
    op.create_unique_constraint(None, 'users', ['oid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_table('group_users')
    op.drop_table('groups')
    # ### end Alembic commands ###
