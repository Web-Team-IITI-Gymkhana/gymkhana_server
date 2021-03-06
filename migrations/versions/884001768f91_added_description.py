"""Added Description

Revision ID: 884001768f91
Revises: 1ad43a925d85
Create Date: 2022-01-26 20:17:35.773186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884001768f91'
down_revision = '1ad43a925d85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hostel', sa.Column('description', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hostel', 'description')
    # ### end Alembic commands ###
