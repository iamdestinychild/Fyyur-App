"""empty message

Revision ID: 5c38432e9267
Revises: 49667ac7bc97
Create Date: 2022-08-18 05:59:43.767779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c38432e9267'
down_revision = '49667ac7bc97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('artists', 'looking_for_venues')
    op.add_column('venues', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.drop_column('venues', 'looking_for_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('looking_for_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('venues', 'seeking_talent')
    op.add_column('artists', sa.Column('looking_for_venues', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('artists', 'seeking_venue')
    # ### end Alembic commands ###