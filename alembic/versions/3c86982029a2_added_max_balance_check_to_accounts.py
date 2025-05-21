"""added max_balance_check to accounts

Revision ID: 3c86982029a2
Revises: d7133dc35b52
Create Date: 2025-05-21 10:20:42.949686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c86982029a2'
down_revision: Union[str, None] = 'd7133dc35b52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        constraint_name="max_balance_check",
        table_name="accounts",
        condition="balance <= 5000000"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        constraint_name="max_balance_check",
        table_name="accounts",
        type_="check"
    )
