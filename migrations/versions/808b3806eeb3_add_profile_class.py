"""Add profile class

Revision ID: 808b3806eeb3
Revises: 9585f4b11867
Create Date: 2024-03-24 01:19:13.725713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '808b3806eeb3'
down_revision = '9585f4b11867'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('sexe', sa.String(length=10), nullable=False),
    sa.Column('birth_date', sa.DateTime(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
