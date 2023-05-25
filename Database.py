import sqlite3
#import data.config
# from backend import UserInterface
class DataBaseConnection:
    # def __init__(self, login, password, path_to_db=data.config.path_to_database):
    #     self.login = login
    #     self.password = password
    #     self.path_to_db = path_to_db

    def __init__(self, path_to_db='data/MainDB.db'):
        # self.login
        # self.password
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    # @staticmethod
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data


class UsersDB:
    def __init__(self, connection: DataBaseConnection):
        # self.login = ""
        # self.password = ""
        self.connection = connection
        self.create_desk()
        # if not self.try_log_in(connection, self.login, self.password):
        #     print('Пользователя с такими данными не существует! Неверный логин или пароль!')
        #     return None
            # raise Exception('Пользователя с такими данными не существует! Неверный логин или пароль!')



    def create_desk(self):
        sql = '''
        create table IF NOT EXISTS `users` (
          `user_id` INTEGER PRIMARY KEY AUTOINCREMENT not null,
          `login` varchar(255) not null,
          `password` varchar(255) not null
        )'''
        self.connection.execute(sql, commit=True)
        return True


    @staticmethod
    def is_login_exist(connection, login):
        # проверяет существует ли пользователь с указанным логином
        sql = "SELECT * FROM users WHERE login=?"
        result = connection.execute(sql, (login,), fetchone=True)

        if result is not None:
            # print("Пользователь с таким логином существует")
            return True  # существует
        else:
            # print("Пользователя с таким логином не существует")
            return False  # не существует


    @staticmethod
    def try_log_in(connection, login, password):
        # проверяет cуществует ли пользователь с логин/пароль
        sql = "SELECT * FROM users WHERE login=? AND password=?"
        result = connection.execute(sql, (login, password), fetchone=True)
        # print("")
        # print(f"result: {result}")
        if result is not None:
            # print("Пользователь с таким логином и паролем существует")
            return True  # существует
        else:
            # print("Пользователя с таким логином и паролем не существует")
            return False  # не существует (Неверен логин/пароль)


    @staticmethod
    def add_new_user(connection, login, password):
        if UsersDB.is_login_exist(connection, login):
            print('Пользователя с таким логином уже существует!')
            return False
        # добавляем в бд нового пользователя
        sql_insert = "INSERT INTO users (login, password) VALUES (?, ?)"
        connection.execute(sql_insert, (login, password), commit=True)
        print("Пользователь успешно добавлен")
        return True


    @staticmethod
    def get_user_login_by_id(connection, id):
        # возвращает логин пользователя по id
        sql = "SELECT login FROM users WHERE user_id =?"
        result = connection.execute(sql, (id,), fetchone=True)
        login = result[0]
        if result is not None:
            # print("Логин пользователя по его id: ")
            return login

    def create_editing_rights_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS `editing_rights` (
            'user_id' INTEGER REFERENCES users(user_id),
            'user_login' VARCHAR(255) REFERENCES users(login),
            'can_edit_desk' BOOLEAN not null,
            'desk_id' INTEGER REFERENCES desk(desk_id)
        )'''
        self.connection.execute(sql, commit=True)

    def get_all_user(self):
        # список всех пользователе (user_id, login)

        sql = "SELECT * FROM users"
        result = self.connection.execute(sql, fetchall=True)
        users = []
        for item in result:
            users.append((
                item[0],
                item[1]
            ))

        return users

    def get_all_user_with_edit_rights(self, desk_id):
        # список всех пользователе (user_id, login, can_edit_desk)
        # can_edit_desk - может ли пользователь редактировать доску с desk_id
        # (актуально только для общественных досок)

        sql = "SELECT * FROM editing_rights WHERE desk_id = ? AND can_edit_desk = 1 "
        result = self.connection.execute(sql, (desk_id,), fetchall=True)
        users = []
        for item in result:
            users.append((
                item[0],
                item[1],
                item[2]
            ))

        return users

    def add_edit_rights_on_public_desk(self, user_id, desk_id):
        # добавляет пользователя права на редактирование публичной доски

        update = "UPDATE editing_rights SET can_edit_desk = 1 WHERE desk_id = ? AND user_id = ?"
        self.connection.execute(update, (desk_id, user_id), commit=True)

        return True

    def del_edit_rights_on_public_desk(self, user_id, desk_id):
        # удаляет пользователя права на редактирование публичной доски

        update = "UPDATE editing_rights SET can_edit_desk = 0 WHERE desk_id = ? AND user_id = ?"
        self.connection.execute(update, (desk_id, user_id), commit=True)

        return True


    @staticmethod
    def get_user_id_by_login(connection, login):
        # возвращает id пользователя по логину (логин уникален для каждого пользователя)
        sql = "SELECT user_id FROM users WHERE login=?"
        result = connection.execute(sql, (login,), fetchone=True)
        id = result[0]
        if result is not None:
            # print("id пользователя по его логину")
            return id


class DesksDB:
    def __init__(self, connection: DataBaseConnection):
        self.connection = connection
        self.create_desk_table()


    def create_desk_table(self):
        sql = '''
        create table IF NOT EXISTS `desks` (
          "desk_id" INTEGER PRIMARY KEY AUTOINCREMENT not null,
          "desk_name" varchar(255) not null,
          "public" BOOLEAN not null,
          "owner_login" varchar(255) REFERENCES users(login)
        )'''
        self.connection.execute(sql, commit=True)
        # создаём доску в бд
        # владелец доски self.login
        # False - доска с таким именем уже существует
        # return True - доска успешно создана

    def create_desk(self, login, desk_name, desk_type=True):
        sql_insert = "INSERT INTO desks (desk_name, public, owner_login) VALUES (?, ?, ?)"
        self.connection.execute(sql_insert, (desk_name, desk_type, login), commit=True)
        print("Доска успешно создана!")
        return True

    def create_columns_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS `columns` (
            `column_id` INTEGER PRIMARY KEY AUTOINCREMENT not null,
            `source_id` INTEGER REFERENCES desks(desk_id),
            `column_name` varchar(255) not null
        )'''
        self.connection.execute(sql, commit=True)
        # print("Таблица колонок успешно создана!")

    def get_owned_desks(self, login):
        sql = "SELECT desk_id, desk_name, public, owner_login FROM desks WHERE owner_login=?"
        result = self.connection.execute(sql, (login,), fetchall=True)
        return result
        # список досок которыми владает пользователь (self.login) в формате (desk_id, desk_name, public, owner_login)


    def get_public_desks(self):
        sql = "SELECT desk_id, desk_name, public, owner_login FROM desks WHERE public=1"
        result = self.connection.execute(sql, fetchall=True)
        return result
        # список публичных досок досок в формате (desk_id, desk_name, public, owner_login)


    def can_edit_desk(self, desk_id, login):
        # можем ли мы редактировать доску
        # доску может редактировать владелец или пользователь из таблицы "права на редактирования"
        sql = "SELECT user_login FROM editing_rights WHERE desk_id = ? AND user_login = ? AND can_edit_desk = 1"
        result = self.connection.execute(sql, (desk_id,login), fetchone=True)
        # TODO: Доделать проверку на наличие прав редактирования из таблицы "права на редактирования"
        if result is not None and result[0] == login:
            return True
        else:
            return False
        return True


    @staticmethod
    def get_desk_name_by_desk_id(connection, desk_id):
        # desk_name - не уникален
        sql = "SELECT desk_name FROM desks WHERE desk_id=?"
        result = connection.execute(sql, (desk_id,), fetchone=True)
        return result[0]


    @staticmethod
     # TODO: Дописать функцию, она свзяана с функцией add_column_to_desk из твоей части
    def get_column_name_by_column_id(connection,column_id):
        sql = "SELECT column_name FROM columns WHERE column_id = ?"
        column_name = connection.execute(sql, (column_id,), fetchone=True)
        # column_name - не уникален
        return column_name


    def change_desk_name(self, desk_id, new_desk_name):
        # изменяем имя доски в бд
        # True - успешно
        # False - доска с таким именем уже существует
        sql = "UPDATE desks SET desk_name = ? WHERE desk_id = ?"
        self.connection.execute(sql, (new_desk_name, desk_id), commit=True)
        print(f"Имя доски изменено на {new_desk_name}!")
        return True

    def create_cards_table(self):
        sql = '''create table IF NOT EXISTS `cards` (
             'card_id' INTEGER PRIMARY KEY AUTOINCREMENT not null,
             'card_title' VARCHAR(255) not null,
             'card_text' VARCHAR(255) not null,
             'card_status' INTEGER not null,
             'card_author_login' VARCHAR(255) REFERENCES users(login),
             'card_desk_id' INTEGER REFERENCES desks(desk_id),
             'card_column_id' INTEGER REFERENCES columns(column_id),
             'card_number_in_column' INTEGER not null
           )'''
        self.connection.execute(sql, commit=True)
        return True

    def del_column(self, column_id):
        # удоляем колонку из бд
        # True - успешно
        sql = "DELETE FROM columns WHERE column_id = ? "
        self.connection.execute(sql, (column_id,), commit=True)
        return True

    def del_desk(self, desk_id):
        # удоляем desk из бд
        # True - успешно
        sql = "DELETE FROM desks WHERE desk_id = ? "
        self.connection.execute(sql, (desk_id,), commit=True)

        return True

    def add_column_to_desk(self, desk_id, column_name):
        # добавляем новый столбец на доску
        # создание новой колонки в бд
        insert = """INSERT INTO columns(source_id,column_name) VALUES (?,?)"""
        self.connection.execute(insert, (desk_id, column_name), commit=True)

        insert = """INSERT INTO cards(card_title,card_text,card_status,card_author_login,card_desk_id,card_column_id,
                card_number_in_column) VALUES (?,?,?,?,?,?,?)"""
        self.connection.execute(insert,("aaa","aa",1,"a", 1, 1,1), commit=True)

        return True

    def add_card_to_column(self, card_title, card_status, card_desk_id, card_column_id,login):
        # добавляем карточку в конец колонки + в бд
        insert = """INSERT INTO cards(card_title,card_text,card_status,card_author_login,card_desk_id,card_column_id,
        card_number_in_column) VALUES (?,?,?,?,?,?,?)"""
        sql = "SELECT card_number_in_column FROM cards WHERE card_column_id = ? and card_desk_id = ?"
        result = self.connection.execute(sql, (card_column_id,card_desk_id), fetchall=True)
        m = []
        last_element = 0
        if result is None:
            number = 1
        else:
            for i in range(len(result)):
                m.append(result[i][0])
                last_element = max(m)
            number = last_element + 1
        self.connection.execute(insert, (card_title, "", card_status, login, card_desk_id, card_column_id,
                                         number),
                                commit=True)
        return True

    def get_desk_card(self, desk_id):
        # возвращает карточки в desk в формате:
        #cards = {
           # ('column_id', 'название столбца'): [
               # ('card_id', 'card_title', 'card_status', 'card_number_in_column'),
                #('0', 'Заголовок', '1', '0'),
           # ]
       # }
        sql = "SELECT column_id FROM columns WHERE source_id = ?"
        numbers = self.connection.execute(sql, (desk_id,), fetchall=True)
        cards = {}

        for item in numbers:
            sql = "SELECT column_id, column_name FROM columns WHERE column_id = ?"
            columns = self.connection.execute(sql, (item[0],), fetchone=True)
            sql = """SELECT card_id, card_title, card_status, card_number_in_column FROM cards WHERE card_desk_id = ? 
            AND card_column_id = ?"""
            cards_in_columns = self.connection.execute(sql, (desk_id,item[0],), fetchall=True)
            cards[columns] = cards_in_columns

        return cards
        #{
            #(22, 'Столбец 1'): [
               # ('0', 'Заголовок 1', '1', '0'),
                #('1', 'Заголовок 2', '1', '1'),
               # ('2', 'Заголовок 3', '2', '3'),
            #],
            #(32, 'Столбец 2'): [
               # ('33', 'Заголовок 1', '0', '0'),
               # ('43', 'Заголовок ttt', '3', '1'),
           # ]
       # }




    def get_full_card_info(self, card_id):

        sql = "SELECT * FROM cards WHERE card_id = ?"
        result = self.connection.execute(sql, (card_id,), fetchall=True)

        if result is None:
            return []
        else:
            card = []

            for item in result:
                card.append({
                    'card_id': item[0],
                    'card_title': item[1],
                    'card_text': item[2],
                    'card_status': item[3],
                    'card_author_login': item[4],
                    'card_desk_id': item[5],
                    'card_column_id': item[6],
                    'card_number_in_column': item[7]
                })
        return card


    def change_card_title(self, card_id, new_title):

        update = "UPDATE cards SET card_title = ? WHERE card_id = ?"
        self.connection.execute(update, (new_title, card_id), commit=True)

        return True


    def change_card_text(self, card_id, new_text):

        update = "UPDATE cards SET card_text = ? WHERE card_id = ?"
        self.connection.execute(update, (new_text, card_id), commit=True)

        return True


    def change_card_status(self, card_id, new_status):

        update = "UPDATE cards SET card_status = ? WHERE card_id = ?"
        self.connection.execute(update, (new_status, card_id), commit=True)

        return True


    def move_card(self, card_id, current_column_id, new_column_id, card_number_in_new_column):
        # перемещает карточку в новый столбец
        # нужно перезаписать card_number_in_column для всех карточек в current_column_id и new_column_id
        sql = "SELECT card_title FROM cards WHERE card_id = ?"
        card_tittle = self.connection.execute(sql, (card_id,), fetchone=True)
        sql = "SELECT card_text FROM cards WHERE card_id = ?"
        card_text = self.connection.execute(sql, (card_id,), fetchone=True)
        sql = "SELECT card_status FROM cards WHERE card_id = ?"
        card_status = self.connection.execute(sql, (card_id,), fetchone=True)
        sql = "SELECT card_author_login FROM cards WHERE card_id = ?"
        card_author_login = self.connection.execute(sql, (card_id,), fetchone=True)
        sql = "SELECT card_desk_id FROM cards WHERE card_id = ?"
        card_desk_id = self.connection.execute(sql, (card_id,), fetchone=True)
        sql = "SELECT card_number_in_column FROM cards WHERE card_id = ?"
        card_number_in_column = self.connection.execute(sql, (card_id,), fetchall=True)

        sql = "DELETE FROM cards WHERE card_id = ?"
        self.connection.execute(sql, (card_id,), commit=True)
        sql = "SELECT card_number_in_column FROM cards WHERE card_column_id = ?"
        result = self.connection.execute(sql,(current_column_id,), fetchall=True)

        for item in range(len(result)):
            if card_number_in_column[0][0] < result[item][0]:
                update = """UPDATE cards SET card_number_in_column = ? WHERE card_number_in_column = ? AND 
                          card_column_id = ?"""
                self.connection.execute(update, (result[item][0]-1, result[item][0], current_column_id), commit=True)

        sql = "SELECT card_number_in_column FROM cards WHERE card_column_id = ?"
        result = self.connection.execute(sql,(new_column_id, ), fetchall=True)

        for item in range(len(result)):
            if card_number_in_new_column <= result[item][0]:
                update = """UPDATE cards SET card_number_in_column = ? WHERE card_number_in_column = ? AND 
                          card_column_id = ?"""
                self.connection.execute(update, (result[item][0]+1, result[item][0], new_column_id), commit=True)
        insert = "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?)"
        self.connection.execute(insert, (card_id, card_tittle, card_text, card_status, card_author_login,
                                         card_desk_id, new_column_id, card_number_in_new_column), commit=True)

        return True

if __name__ == '__main__':
    conn1 = DataBaseConnection()
    user1 = UsersDB(conn1)
    desk1 = DesksDB(conn1)
    # user1.add_new_user(conn1, "Sergey", "Pristup")
    # user1.add_new_user(conn1, "Misha", "Elkin")
    # user1.add_new_user(conn1, "Gleb", "Kim")
    # desk1.create_desk("Sergey desk", "Sergey", 1)
    # desk1.create_desk("Sergey desk2", "Sergey", 1)
    # desk1.create_desk("Misha desk3", "Misha", 1)
    # print(desk1.get_owned_desks("Misha"))