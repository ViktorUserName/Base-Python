import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, CheckConstraint, Text, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, scoped_session


engine = create_engine("postgresql://postgres:postgres@localhost:5432/coinkeeper", echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    balance = Column(Numeric(15, 2), nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    categories = relationship("Categories", back_populates="users")
    transactions = relationship("Transactions", back_populates="users")

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    users = relationship("Users", back_populates="categories")
    transactions = relationship("Transactions", back_populates="categories")

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_type = Column(String(30), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    users = relationship("Users", back_populates="transactions")
    categories = relationship("Categories", back_populates="transactions")

    __table_args__ = (
        CheckConstraint(
            "transaction_type IN ('income', 'expense')",
            name='check_transaction_type'
        ),
    )

def init_db():
    Base.metadata.create_all(engine, checkfirst=True)
