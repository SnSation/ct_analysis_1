"""empty message

Revision ID: 180ad8812f22
Revises: dfc7a0707227
Create Date: 2020-12-12 15:37:17.249907

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '180ad8812f22'
down_revision = 'dfc7a0707227'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cohort',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('instructor', sa.String(length=50), nullable=True),
    sa.Column('curriculum', sa.String(length=50), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('curriculum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('likelihood', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instructor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('quality', sa.Float(), nullable=True),
    sa.Column('commitment', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('intelligence', sa.Integer(), nullable=True),
    sa.Column('commitment', sa.Integer(), nullable=True),
    sa.Column('background', sa.Integer(), nullable=True),
    sa.Column('understanding', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('difficulty', sa.Float(), nullable=True),
    sa.Column('prerequisite', sa.Integer(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('instructors')
    op.drop_table('classes')
    op.drop_table('cohorts')
    op.drop_table('topics')
    op.drop_table('events')
    op.drop_table('students')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('intelligence', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('commitment', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('background', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('understanding', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='students_pkey')
    )
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('likelihood', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='events_pkey')
    )
    op.create_table('topics',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('difficulty', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('prerequisite', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='topics_pkey')
    )
    op.create_table('cohorts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('instructor', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('curriculum', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('student', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cohorts_pkey')
    )
    op.create_table('classes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('topic', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='classes_pkey')
    )
    op.create_table('instructors',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('quality', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('commitment', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='instructors_pkey')
    )
    op.drop_table('topic')
    op.drop_table('student')
    op.drop_table('instructor')
    op.drop_table('event')
    op.drop_table('curriculum')
    op.drop_table('cohort')
    # ### end Alembic commands ###
