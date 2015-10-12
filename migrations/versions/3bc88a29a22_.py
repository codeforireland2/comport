"""empty message

Revision ID: 3bc88a29a22
Revises: 2de736b481
Create Date: 2015-10-12 14:53:43.063336

"""

# revision identifiers, used by Alembic.
revision = '3bc88a29a22'
down_revision = '2de736b481'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('citizen_complaints', 'officer_years_of_service')
    op.add_column('citizen_complaints', sa.Column('officer_years_of_service', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('citizen_complaints', 'officer_years_of_service')
    op.add_column('citizen_complaints', sa.Column('officer_years_of_service', sa.Integer(), nullable=True))
    ### end Alembic commands ###
