from database.models import User
from database import get_db
from datetime import datetime


# Регистрация
def register_user_db(name, lastname, phone_number, email, password, country):
    db = next(get_db())
    new_user = User(name=name, lastname=lastname, phone_number=phone_number,
                    email=email, password=password,
                    reg_date=datetime.now(), country=country)
    db.add(new_user)
    db.commit()
    return 'Пользователь успешно зарегистрирован'


# Получить информацию опред пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'Что пошло не так'


# Получить всех пользователей
def get_all_user_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Валидация email
def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return 'Что пошло не так'


# Изменить данные определ пользователя
def edit_user_db(user_id, edit_info, new_info):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        if edit_info == 'email':
            exact_user.email = new_info
        elif edit_info == 'country':
            exact_user.country = new_info
        else:
            return 'Нет такой команды'

        db.commit()
        return 'Данные успешно обновлены'
    else:
        return 'Пользователь не найден'


# Удаление пользователя
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        return 'Пользователь не найден'
    else:
        db.delete(user)
        db.commit()
        return 'Успешно удален'
