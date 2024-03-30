from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base


# Таблица для пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    lastname = Column(String)
    phone_number = Column(Integer, unique=True)
    email = Column(String, unique=True)
    country = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


# Таблица для карт
class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_name = Column(String, ForeignKey('users.name'))
    card_number = Column(Integer, nullable=False, unique=True)
    balance = Column(Float, default=0)
    cvv = Column(Integer)
    exp_date = Column(Integer)

    user_fk = relationship(User, lazy='subquery')


# Таблица транзакция (История транзакция)
class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_from_number = Column(Integer, ForeignKey('cards.card_number'))
    card_to_number = Column(Integer, ForeignKey('cards.card_number'))
    amount = Column(Float)
    status = Column(Boolean, default=True)
    transaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, lazy='subquery')
    card_to_fk = relationship(UserCard, lazy='subquery')
