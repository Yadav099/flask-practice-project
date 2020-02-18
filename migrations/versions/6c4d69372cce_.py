"""empty message

Revision ID: 6c4d69372cce
Revises: 2a73cdac7009
Create Date: 2020-02-18 16:26:20.515070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c4d69372cce'
down_revision = '2a73cdac7009'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('e_password', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'e_password')
    # ### end Alembic commands ###
