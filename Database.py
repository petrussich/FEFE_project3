import sqlite3
import data.config
# from backend import UserInterface
class DataBaseConnection:
    # def __init__(self, login, password, path_to_db=data.config.path_to_database):
    #     self.login = login
    #     self.password = password
    #     self.path_to_db = path_to_db

    def __init__(self, path_to_db=data.config.path_to_database):
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
        sql = "SELECT owner_login FROM desks WHERE desk_id=?"
        result = self.connection.execute(sql, (desk_id,), fetchone=True)
        # TODO: Доделать проверку на наличие прав редактирования из таблицы "права на редактирования"
        if result is not None and result[0] == login:
            return True
        else:
            return False


    @staticmethod
    def get_desk_name_by_desk_id(connection, desk_id):
        # desk_name - не уникален
        sql = "SELECT desk_name FROM desks WHERE desk_id=?"
        result = connection.execute(sql, (desk_id,), fetchone=True)
        return result[0]


    @staticmethod
     # TODO: Дописать функцию, она свзяана с функцией add_column_to_desk из твоей части
    def get_column_name_by_column_id(column_id):

        # column_name - не уникален
        return 'column_name'


    def change_desk_name(self, desk_id, new_desk_name):
        # изменяем имя доски в бд
        # True - успешно
        # False - доска с таким именем уже существует
        sql = "UPDATE desks SET desk_name = ? WHERE desk_id = ?"
        self.connection.execute(sql, (new_desk_name, desk_id), commit=True)
        print(f"Имя доски изменено на {new_desk_name}!")
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