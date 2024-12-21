"""Initial migration.

Revision ID: 5782de728d40
Revises: 
Create Date: 2024-12-20 23:13:03.179155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5782de728d40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('aluno', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_aluno_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_aluno_nome'), ['nome'], unique=True)

    op.create_table('presenca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_hora', sa.DateTime(), nullable=True),
    sa.Column('aluno_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aluno_id'], ['aluno.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('presenca', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_presenca_data_hora'), ['data_hora'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('presenca', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_presenca_data_hora'))

    op.drop_table('presenca')
    with op.batch_alter_table('aluno', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_aluno_nome'))
        batch_op.drop_index(batch_op.f('ix_aluno_email'))

    op.drop_table('aluno')
    # ### end Alembic commands ###
