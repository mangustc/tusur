"""create second migration

Revision ID: 1214901947ad
Revises: 0b2f49e220cd
Create Date: 2024-10-12 16:55:42.839627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1214901947ad'
down_revision: Union[str, None] = '0b2f49e220cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
