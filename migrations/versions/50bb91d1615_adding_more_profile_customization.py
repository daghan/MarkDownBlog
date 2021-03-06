"""adding_more_profile_customization

Revision ID: 50bb91d1615
Revises: 13234475ad5
Create Date: 2015-05-11 21:04:17.237732

"""

# revision identifiers, used by Alembic.
revision = '50bb91d1615'
down_revision = '13234475ad5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('github_url', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('gplus_url', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('linkedin_url', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('twitter_url', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'twitter_url')
    op.drop_column('user', 'linkedin_url')
    op.drop_column('user', 'gplus_url')
    op.drop_column('user', 'github_url')
    ### end Alembic commands ###
