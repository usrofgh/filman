"""empty message

Revision ID: c51cb3179d6f
Revises: 2f7d53303828
Create Date: 2025-04-25 01:09:41.130314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c51cb3179d6f'
down_revision: Union[str, None] = '2f7d53303828'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_url')
    # ### end Alembic commands ###
