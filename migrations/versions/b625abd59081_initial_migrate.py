"""initial migrate

Revision ID: b625abd59081
Revises: 8bf17eba3817
Create Date: 2025-04-15 15:36:04.882072

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b625abd59081'
down_revision = '8bf17eba3817'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', mysql.ENUM('admin', 'user'), nullable=True))

    # ### end Alembic commands ###
