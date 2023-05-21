from Database import UsersDB, DesksDB, DataBaseConnection

connect = DataBaseConnection("Roma", "Slepchenko")
db_of_users = UsersDB(connect)
db_of_desks = DesksDB(connect)

db_of_users.add_new_user(connect, "Roma", "Slepchenko")
db_of_users.add_new_user(connect, "Sergey", "Pristup")
# UsersDB.add_new_user(conn1, "Gleb", "Kim")

desk1 = DesksDB(connect)
desk1.create_desk("first desk", 1)
desk1.create_desk("second_desk", 0)
desk1.create_desk("third_desk", 1)
# desk1.create_columns_table()
desk1.change_desk_name(1, "new_name")