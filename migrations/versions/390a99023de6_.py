"""empty message

Revision ID: 390a99023de6
Revises: d71fdb66e31f
Create Date: 2020-02-19 01:23:45.617311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '390a99023de6'
down_revision = 'd71fdb66e31f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phonenumber', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phonenumber')
    # ### end Alembic commands ###