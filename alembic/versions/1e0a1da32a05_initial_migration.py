"""Initial Migration

Revision ID: 1e0a1da32a05
Revises: 
Create Date: 2024-12-24 20:47:38.343008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e0a1da32a05'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cs_grp_m',
    sa.Column('id', sa.BigInteger(), sa.Identity(always=False, start=1, cycle=False), nullable=False),
    sa.Column('cs_grp_code', sa.String(length=255), nullable=True),
    sa.Column('cs_grp_name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True, comment='1=Active,0=Inactive'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.BigInteger(), nullable=True),
    sa.Column('updated_by', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='cs_grp_m_pkey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cs_grp_m')
    # ### end Alembic commands ###