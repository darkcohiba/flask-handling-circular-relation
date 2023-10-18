"""empty message

Revision ID: b670aedfd471
Revises: 
Create Date: 2023-10-18 16:05:03.372239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b670aedfd471'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users_table')),
    sa.UniqueConstraint('username', name=op.f('uq_users_table_username'))
    )
    op.create_table('movies_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users_table.id'], name=op.f('fk_movies_table_created_by_users_table')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_movies_table'))
    )
    op.create_table('reviews_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies_table.id'], name=op.f('fk_reviews_table_movie_id_movies_table')),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], name=op.f('fk_reviews_table_user_id_users_table')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews_table'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews_table')
    op.drop_table('movies_table')
    op.drop_table('users_table')
    # ### end Alembic commands ###
