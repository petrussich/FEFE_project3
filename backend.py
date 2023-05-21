# сюда нужно импортировать классы бд
from loader import connect, db_of_users, db_of_desks


class UserInterface:
    def __init__(self, login, password):
        if not self.try_log_in(login, password):
            raise Exception('Пользователя с такими данными не существует! Неверен логин/пароль!')
        self.login = login
        self.password = password

    @staticmethod
    def is_login_exist(login):
        connection_users = connect
        users = db_of_users.is_login_exist(connection_users, login)
        if users:
            return True
        else:
            return False
        # проверяет существует ли пользователь с указанным логином
        # True - существует
        # False - нет существует


    @staticmethod
    def try_log_in(login, password):
        connection_users = connect
        users = db_of_users.try_log_in(connection_users, login, password)
        if users:
            return True
        else:
            return False
        # проверяет cуществует ли пользователь с логин/пароль
        # True - существует
        # False - нет существует (Неверен логин/пароль)
        # return True

    @staticmethod
    def add_new_user(login, password):
        connection_users = connect
        users = db_of_users.add_new_user(connection_users, login, password)
        if users:
            return True
        else:
            return False
        # добавляем в бд нового пользователя
        # return True

    @staticmethod
    def get_user_login_by_id(id):
        # возвращает логин пользователя по id
        connection_users = connect
        users = db_of_users.get_user_login_by_id(connection_users, id)
        return users
        # return 'login'

    @staticmethod
    def get_user_id_by_login(login):
        connection_users = connect
        users = db_of_users.get_user_id_by_login(connection_users, login)
        return users
        # возвращает id пользователя по логину (логин уникален для каждого пользователя)
        # return 1

    def create_desk(self, desk_name, desk_type):
        users = db_of_desks.create_desk(desk_name, desk_type)
        # создаём доску в бд
        # владелец доски self.login
        # True - доска успешно создана
        # False - доска с таким именем уже существует
        return True

    def get_owned_desks(self):
        # список досок которыми владает пользователь (self.login) в формате (desk_id, desk_name, public, owner_login)
        print(f'Получаем список досок для {self.login}')
        users = db_of_desks.get_owned_desks()
        return users
        # return [(0, 'Доска 1', 0, 'Myself'), (1, 'Доска для 2112', 1, 'Myself')]

    def get_public_desks(self):
        # список публичных досок досок в формате (desk_id, desk_name, public, owner)
        users = db_of_desks.get_public_desks()
        return users
        # return [(33, 'Доска 333', 1, 'Sera'), (222, 'Доска 77', 1, 'Bob')]

    def can_edit_desk(self, desk_id):
        # можем ли мы редактировать доску
        # доску может редактировать владелец или пользователь из таблицы "права на редактирования"
        users = db_of_desks.can_edit_desk(desk_id)
        if users:
            return True
        else:
            return False

    @staticmethod
    def get_desk_name_by_desk_id(desk_id):
        # desk_name - не уникален
        connection_users = connect
        users = db_of_desks.get_desk_name_by_desk_id(connection_users, desk_id)
        return users
        # return 'desk_name'

    @staticmethod
    # TODO: дописать функцию
    def get_column_name_by_column_id(column_id):
        # column_name - не уникален
        return 'column_name'

    def change_desk_name(self, desk_id, new_desk_name):
        # изменяем имя доски в бд
        # True - успешно
        # False - доска с таким именем уже существует
        users = db_of_desks.change_desk_name(desk_id, new_desk_name)
        return True

    def change_column_name(self, column_id, new_column_name):
        # изменяем имя column в бд
        # True - успешно
        return True

    def del_column(self, column_id):
        # удоляем колонку из бд
        # True - успешно
        return True

    def del_desk(self, desk_id):
        # удоляем desk из бд
        # True - успешно
        return True

    def add_column_to_desk(self, desk_id, column_name):
        # добавляем новый столбец на доску
        # создание новой колонки в бд
        return True

    def add_card_to_column(self, card_title, card_status, card_desk_id, card_column_id):
        # добавляем карточку в конец колонки + в бд
        return True

    def get_desk_card(self, desk_id):
        # возвращает карточки в desk в формате:
        cards = {
            ('column_id', 'название столбца'): [
                ('card_id', 'card_title', 'card_status', 'card_number_in_column'),
                ('0', 'Заголовок', '1', '0'),
            ]
        }
        return {
            (22, 'Столбец 1'): [
                ('0', 'Заголовок 1', '1', '0'),
                ('1', 'Заголовок 2', '1', '1'),
                ('2', 'Заголовок 3', '2', '3'),
            ],
            (32, 'Столбец 2'): [
                ('33', 'Заголовок 1', '0', '0'),
                ('43', 'Заголовок ttt', '3', '1'),
            ]
        }

    def get_full_card_info(self, card_id):
        return {
            'card_id': '11',
            'card_title': 'Title 555',
            'card_text': 'lorem text',
            'card_status': 2,
            'card_author_login': 'Sergey',
            'card_desk_id': 3,
            'card_column_id': 333,
            'card_number_in_column': 33
        }

    def change_card_title(self, card_id, new_title):
        return True

    def change_card_text(self, card_id, new_text):
        return True

    def change_card_status(self, card_id, new_status):
        return True

    def move_card(self, card_id, current_column_id, new_column_id, card_number_in_new_column):
        # перемещает карточку в новый столбец
        # нужно перезаписать card_number_in_column для всех карточек в current_column_id и new_column_id
        return True

    def add_edit_rights_on_public_desk(self, user_id, desk_id):
        # добавляет пользователя права на редактирование публичной доски
        return True

    def del_edit_rights_on_public_desk(self, user_id, desk_id):
        # удаляет пользователя права на редактирование публичной доски
        return True

    def get_all_user(self):
        # список всех пользователе (user_id, login)
        users = db_of_users.get_all_users()
        # return users
        # return [(1, 'Bob'), (3, 'Sera')]

    def get_all_user_with_edit_rights(self, desk_id):
        # список всех пользователе (user_id, login, can_edit_desk)
        # can_edit_desk - может ли пользователь редактировать доску с desk_id
        # (актуально только для общественных досок)
        return [(1, 'Bob', 0), (3, 'Sera', 1), (33, 'Pol', 1)]

#