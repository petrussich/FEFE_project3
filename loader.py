from Database import UsersDB, DesksDB, DataBaseConnection

connect = DataBaseConnection("Roma", "Slepchenko")
db_of_users = UsersDB(connect)
db_of_desks = DesksDB(connect)

