"""empty message

Revision ID: bec2e53ada94
Revises: 6c4d69372cce
Create Date: 2020-02-18 17:23:50.296377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bec2e53ada94'
down_revision = '6c4d69372cce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mail_template',
    sa.Column('h_id', sa.Integer(), nullable=False),
    sa.Column('html', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('h_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mail_template')
    # ### end Alembic commands ###