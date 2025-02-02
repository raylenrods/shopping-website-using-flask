"""Added ManyToMany

Revision ID: 35e093220ba7
Revises: a71932e2c4b2
Create Date: 2022-06-11 21:54:45.789387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35e093220ba7'
down_revision = 'a71932e2c4b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cart',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.pid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Cart')
    # ### end Alembic commands ###
