"""revision_name

Revision ID: 75e483e9733e
Revises: 2ab220b421de
Create Date: 2024-08-26 14:18:22.650684

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision = '75e483e9733e'
down_revision = '2ab220b421de'
branch_labels = None
depends_on = None

def upgrade():
    # Add a new column to the table
    op.add_column('user', sa.Column('referral_id', sa.Integer(), nullable=True))
    
    # Create a foreign key relationship to the same table
    op.create_foreign_key(
        'fk_referral_user', 'user', 'user', ['referral_id'], ['id']
    )

def downgrade():
    # Drop the foreign key constraint
    op.drop_constraint('fk_referral_user', 'user', type_='foreignkey')
    
    # Drop the new column
    op.drop_column('user', 'referral_id')

    
    # Revert any other changes here if needed
