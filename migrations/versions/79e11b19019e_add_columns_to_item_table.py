"""Add columns to item table

Revision ID: 79e11b19019e
Revises: b80c4fe35a61
Create Date: 2019-07-17 10:59:48.989905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79e11b19019e'
down_revision = 'b80c4fe35a61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_item', sa.Column('cleared', sa.Boolean(), nullable=False))
    op.add_column('t_item', sa.Column('counter', sa.Integer(), nullable=False))
    op.add_column('t_item', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('t_item', sa.Column('t_user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 't_item', 't_user', ['t_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 't_item', type_='foreignkey')
    op.drop_column('t_item', 't_user_id')
    op.drop_column('t_item', 'created_at')
    op.drop_column('t_item', 'counter')
    op.drop_column('t_item', 'cleared')
    # ### end Alembic commands ###
