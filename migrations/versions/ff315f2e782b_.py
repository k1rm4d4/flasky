"""add email and password for user

Revision ID: ff315f2e782b
Revises: ac6a7cfd3d1b
Create Date: 2024-04-14 12:02:47.675273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff315f2e782b'
down_revision = 'ac6a7cfd3d1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=64), nullable=True))
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.drop_column('email')

    # ### end Alembic commands ###