"""Add Task model

Revision ID: 096b857ae820
Revises: 2e95275cf118
Create Date: 2024-03-23 17:45:37.573335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '096b857ae820'
down_revision = '3ab63544ce9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
