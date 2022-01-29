"""Add event table

Revision ID: 466490b24957
Revises: 201299b6454c
Create Date: 2022-01-29 03:16:33.843348

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '466490b24957'
down_revision = '201299b6454c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('notify', sa.Boolean(), nullable=False),
    sa.Column('is_online', sa.Boolean(), nullable=False),
    sa.Column('meet_link', sa.String(length=255), nullable=True),
    sa.Column('venue', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###
