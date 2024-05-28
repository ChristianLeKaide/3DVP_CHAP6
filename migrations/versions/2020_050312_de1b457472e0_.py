"""empty message

Revision ID: de1b457472e0
Revises: f939d67374e4
Create Date: 2020-05-03 12:02:11.958152

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de1b457472e0'
down_revision = 'f939d67374e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('custom_domain', sa.Column('dmarc_verified', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('custom_domain', 'dmarc_verified')
    # ### end Alembic commands ###
