"""empty message

Revision ID: d7e1a6d1747d
Revises: 
Create Date: 2019-02-11 07:33:24.503569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7e1a6d1747d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=250), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('map',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('map_file', sa.Text(), nullable=True),
    sa.Column('border_N', sa.Float(), nullable=True),
    sa.Column('border_S', sa.Float(), nullable=True),
    sa.Column('border_E', sa.Float(), nullable=True),
    sa.Column('border_W', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['area.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('trail',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('map_id', sa.Integer(), nullable=False),
    sa.Column('file', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['map_id'], ['map.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trail')
    op.drop_table('map')
    op.drop_table('user')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
