"""Adicionar coluna emprestado_para

Revision ID: 7daddb9bb71a
Revises: 5af8194ab65e
Create Date: 2023-11-21 11:18:09.304628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7daddb9bb71a'
down_revision = '5af8194ab65e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livros', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emprestado_para', sa.String(length=255), nullable=True))

    with op.batch_alter_table('livros_emprestados', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_devolucao', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livros_emprestados', schema=None) as batch_op:
        batch_op.drop_column('data_devolucao')

    with op.batch_alter_table('livros', schema=None) as batch_op:
        batch_op.drop_column('emprestado_para')

    # ### end Alembic commands ###
