"""create books table

Revision ID: 20241124_0001
Revises:
Create Date: 2025-11-24 00:00:00
"""

from alembic import op
import sqlalchemy as sa


revision = "20241124_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("author", sa.String(), nullable=False),
        sa.Column("language", sa.String(), nullable=False),
    )
    op.create_index("ix_books_title", "books", ["title"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_books_title", table_name="books")
    op.drop_table("books")

