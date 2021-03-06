"""empty message

Revision ID: 33fd688a2a45
Revises: 92d704fa40f2
Create Date: 2020-02-19 10:43:50.063905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33fd688a2a45'
down_revision = '92d704fa40f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('purchaseDate', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'purchaseDate')
    # ### end Alembic commands ###
