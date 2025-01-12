"""emp_m migration

Revision ID: a10a4c670d00
Revises: e861203540a7
Create Date: 2025-01-07 10:47:08.726318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a10a4c670d00'
down_revision: Union[str, None] = 'e861203540a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emp_m',
    sa.Column('id', sa.BigInteger(), sa.Identity(always=False, start=1, cycle=False), nullable=False),
    sa.Column('emp_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('mobile', sa.String(length=25), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True, comment='1=Active,0=Inactive'),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('remember_token', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='emp_m_pkey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emp_m')
    # ### end Alembic commands ###
