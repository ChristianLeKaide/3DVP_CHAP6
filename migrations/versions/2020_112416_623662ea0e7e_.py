"""empty message

Revision ID: 623662ea0e7e
Revises: d1edb3cadec8
Create Date: 2020-11-24 16:34:02.327556

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623662ea0e7e'
down_revision = 'd1edb3cadec8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_log', sa.Column('mailbox_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'email_log', 'mailbox', ['mailbox_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'email_log', type_='foreignkey')
    op.drop_column('email_log', 'mailbox_id')
    # ### end Alembic commands ###
