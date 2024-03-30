from database import get_db
from database.models import Transaction, UserCard
from datetime import datetime


# Проверка карты
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()
    return exact_card


# Создание перевода
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличии обеих карт в БД
    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)

    # Если обе карты сущ в БД, то делаем транзакцию (перевод)

    if check_card_to and check_card_from:
        # Проверить баланс отправителя
        if check_card_from.balance >= amount:
            # Минусуем у того кто отправляет деньги
            check_card_from.balance -= amount
            # Добавляем тому кто получает
            check_card_to.balance += amount

            # Сохраняем платеж в БД
            new_transaction = Transaction(card_from_number=check_card_from.card_number,
                                          card_to_number=check_card_to.card_number,
                                          amount=amount,
                                          transaction_date=datetime.now())
            db.add(new_transaction)
            db.commit()

            return 'Перевод успешно выполнен!'
        else:
            return 'Не достаточно средств на балансе'
    else:
        return 'Одна из карт не существует!'


# Получить все переводы по карте, то есть История
def get_history_transaction(card_from_number):
    db = next(get_db())
    card_transaction = db.query(Transaction).filter_by(card_from_number=card_from_number).all()

    if card_transaction:
        return card_transaction
    else:
        return 'Нету истории!'


# Отмена транзакции
def cancel_transaction_db(card_from, card_to, amount,transaction_id):
    db = next(get_db())

    # Проверка на наличие обеих карт в БД
    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)
    if checker_card_from and checker_card_to:
        transaction_to_cancel = db.query(Transaction).filter_by(transaction_id=transaction_id).first()
        if transaction_to_cancel:
            checker_card_from.balance += amount
            checker_card_to.balance -= amount
            transaction_to_cancel.status = False

            db.delete(transaction_to_cancel)
            db.commit()
            return 'Перевод отменен'
        else:
            return 'Указанный перевод не существует!'
    else:
        return 'Одна из карт не существуют'
