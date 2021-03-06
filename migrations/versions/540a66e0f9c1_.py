"""empty message

Revision ID: 540a66e0f9c1
Revises: bec2e53ada94
Create Date: 2020-02-18 23:38:29.622652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '540a66e0f9c1'
down_revision = 'bec2e53ada94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mail_template', sa.Column('html_first', sa.String(length=128), nullable=True))
    op.add_column('mail_template', sa.Column('html_last', sa.String(length=128), nullable=True))
    op.add_column('mail_template', sa.Column('html_middle', sa.String(length=128), nullable=True))
    op.drop_column('mail_template', 'html')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mail_template', sa.Column('html', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('mail_template', 'html_middle')
    op.drop_column('mail_template', 'html_last')
    op.drop_column('mail_template', 'html_first')
    # ### end Alembic commands ###
