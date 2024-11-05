"""create third migration

Revision ID: 746829b91540
Revises: 1214901947ad
Create Date: 2024-10-12 16:57:24.452353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '746829b91540'
down_revision: Union[str, None] = '1214901947ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
