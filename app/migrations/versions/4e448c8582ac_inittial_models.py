"""Inittial models

Revision ID: 4e448c8582ac
Revises: 
Create Date: 2024-11-29 22:34:36.964314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e448c8582ac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cables',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('index', sa.String(), nullable=False),
    sa.Column('group', sa.String(), nullable=False),
    sa.Column('assembly', sa.String(), nullable=False),
    sa.Column('factory_number', sa.String(), nullable=False),
    sa.Column('last_service', sa.TIMESTAMP(), nullable=False),
    sa.Column('next_service', sa.TIMESTAMP(), nullable=False),
    sa.Column('status', sa.Enum('AVAILABLE', 'ISSUED', 'ON_SERVICE', name='status'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('issued_by', sa.Uuid(), nullable=False),
    sa.Column('return_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('factory_employee_id', sa.Integer(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('role', sa.Enum('USER', 'MODERATOR', 'ADMIN', name='role'), server_default='USER', nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_users_factory_employee_id'), 'users', ['factory_employee_id'], unique=True)
    op.create_table('profiles',
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('patronymic', sa.String(), nullable=False),
    sa.Column('division', sa.Enum('LAB1', 'LAB2', 'LAB3', 'LAB5', 'LAB6', 'LAB7', 'LAB8', 'PDB', name='division'), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_index(op.f('ix_users_factory_employee_id'), table_name='users')
    op.drop_table('users')
    op.drop_table('transactions')
    op.drop_table('cables')
    # ### end Alembic commands ###
