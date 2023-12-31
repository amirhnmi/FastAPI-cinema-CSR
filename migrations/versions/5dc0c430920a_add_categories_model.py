"""add categories model

Revision ID: 5dc0c430920a
Revises: ae546f36c460
Create Date: 2023-08-25 10:54:24.676837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dc0c430920a'
down_revision: Union[str, None] = 'ae546f36c460'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artandexpriences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('image', sa.String(length=250), nullable=False),
    sa.Column('director', sa.String(length=100), nullable=False),
    sa.Column('actors', sa.String(length=250), nullable=False),
    sa.Column('producer', sa.String(length=100), nullable=False),
    sa.Column('production_date', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('childrenstheaters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('image', sa.String(length=250), nullable=False),
    sa.Column('director', sa.String(length=100), nullable=False),
    sa.Column('actors', sa.String(length=250), nullable=False),
    sa.Column('producer', sa.String(length=100), nullable=False),
    sa.Column('production_date', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comedytheaters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('image', sa.String(length=250), nullable=False),
    sa.Column('director', sa.String(length=100), nullable=False),
    sa.Column('actors', sa.String(length=250), nullable=False),
    sa.Column('producer', sa.String(length=100), nullable=False),
    sa.Column('production_date', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('screenings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('image', sa.String(length=250), nullable=False),
    sa.Column('director', sa.String(length=100), nullable=False),
    sa.Column('actors', sa.String(length=250), nullable=False),
    sa.Column('producer', sa.String(length=100), nullable=False),
    sa.Column('production_date', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theaters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('image', sa.String(length=250), nullable=False),
    sa.Column('director', sa.String(length=100), nullable=False),
    sa.Column('actors', sa.String(length=250), nullable=False),
    sa.Column('producer', sa.String(length=100), nullable=False),
    sa.Column('production_date', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('theaters')
    op.drop_table('screenings')
    op.drop_table('comedytheaters')
    op.drop_table('childrenstheaters')
    op.drop_table('artandexpriences')
    # ### end Alembic commands ###
