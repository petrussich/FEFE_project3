from tkinter import *
from tkinter import messagebox
from backend import UserInterface

def Start(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем приветственный текст
    label_welcome = Label(window, text="Добро пожаловать в TaskManager!", bg="#D7E3F5", fg="#043C66", font=("Arial Black", 16))

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_login = Button(window, text="Вход", command=lambda: Login(window), **button_style)
    button_register = Button(window, text="Регистрация", command=lambda: SignUp(window), **button_style)

    # задаем размеры кнопок
    button_login.config(width=15, height=1)
    button_register.config(width=15, height=1)

    # располагаем кнопки и текст
    label_welcome.place(relx=0.5, rely=0.3, anchor="center")
    button_login.place(relx=0.5, rely=0.5, anchor="center")
    button_register.place(relx=0.5, rely=0.7, anchor="center")

def Login(window):
    login=''
    password=''
    def try_to_login(login,password):
        if UserInterface.try_log_in(login, password):
            user_interface = UserInterface(login, password)
            Menu(window, user_interface)
        else:
            messagebox.showerror('Ошибка', 'Неверный логин или пароль')
            Login(window)

    # удаляем элементы окна стартового меню
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем текстовые поля
    label_username = Label(window, text="Логин:", **label_style)
    label_password = Label(window, text="Пароль:", **label_style)

    # создаем поля для ввода
    entry_username = Entry(window, textvariable=login, **entry_style)
    entry_password = Entry(window, show="*", textvariable=password, **entry_style)

    # располагаем текст и поля для ввода
    label_username.place(relx=0.38, rely=0.4, anchor="e")
    entry_username.place(relx=0.4, rely=0.4, anchor="w")
    label_password.place(relx=0.38, rely=0.5, anchor="e")
    entry_password.place(relx=0.4, rely=0.5, anchor="w")

    # создаем стиль для кнопки
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_login = Button(window, text="Вход", command = lambda: try_to_login(login,password),  **button_style)
    button_back = Button(window, text="Назад", command = lambda: Start(window), **button_style)

    # задаем размеры кнопок
    button_login.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_login.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def SignUp(window):
    login = StringVar()
    password = StringVar()
    password2 = StringVar()

    def try_to_signup(login, password, password2):
        if not (UserInterface.is_login_exist(login)) and (password.get() == password2.get()):
            UserInterface.add_new_user(login.get(), password.get())
            user_interface = UserInterface(login.get(), password.get())
            Menu(window, user_interface)
        elif password.get() != password2.get():
            messagebox.showerror('Ошибка', 'Пароли не совпадают')
            SignUp(window)
        elif UserInterface.is_login_exist(login):
            messagebox.showerror('Ошибка', 'Пользователь с таким логином уже существует')
            SignUp(window)

    # удаляем элементы окна стартового меню
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем текстовые поля
    label_login = Label(window, text="Логин:", **label_style)
    label_password = Label(window, text="Пароль:", **label_style)
    label_password2 = Label(window, text="Повторите пароль:", **label_style)

    # создаем поля для ввода
    entry_login = Entry(window, textvariable=login, **entry_style)
    entry_password = Entry(window, textvariable=password, show="*", **entry_style)
    entry_password2 = Entry(window, textvariable=password2, show="*", **entry_style)

    # располагаем текст и поля для ввода
    label_login.place(relx=0.42, rely=0.35, anchor="e")
    entry_login.place(relx=0.45, rely=0.35, anchor="w")
    label_password.place(relx=0.42, rely=0.45, anchor="e")
    entry_password.place(relx=0.45, rely=0.45, anchor="w")
    label_password2.place(relx=0.42, rely=0.55, anchor="e")
    entry_password2.place(relx=0.45, rely=0.55, anchor="w")

    # создаем стиль для кнопки
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_signup = Button(window, text="Зарегистрироваться", command=lambda: try_to_signup(login, password, password2), **button_style)
    button_back = Button(window, text="Назад", command=lambda: Start(window), **button_style)
    button_signup.config(width=20, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_signup.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def Menu(window, user_interface):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_mydesks = Button(window, text="Мои доски", command=lambda: DesksList(window, user_interface, user_interface.get_owned_desks()), **button_style)
    button_commondesks = Button(window, text="Общие доски", command=lambda: DesksList(window, user_interface, user_interface.get_public_desks()), **button_style)
    button_newdesk = Button(window, text="Создать доску", command=lambda: NewDesk(window, user_interface), **button_style)
    button_back = Button(window, text="Выйти", command = lambda: Start(window), **button_style)

    # задаем размеры кнопок
    button_mydesks.config(width=15, height=1)
    button_commondesks.config(width=15, height=1)
    button_newdesk.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_mydesks.place(relx=0.5, rely=0.3, anchor="center")
    button_commondesks.place(relx=0.5, rely=0.5, anchor="center")
    button_newdesk.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def DesksList(window, user_interface, desks):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    desks = [(0, 'Доска 1', 0, 'Myself'), (1, 'Доска для 2112', 1, 'хйу') , (2, 'Нееееет', 1, 'bob') , (3, 'ДОСКА', 0, 'хйу') , (4, 'Доска для 2112', 0, 'Adasd')]

    if len(desks) > 0:
        # создаем кнопки
        button_back = Button(window, text="Назад", command=lambda: Menu(window, user_interface), **button_style)
        button_desks = []

        # создаем контейнер для кнопок с возможностью прокрутки
        canvas = Canvas(window, bg='#D7E3F5')
        scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
        frame = Frame(canvas)
        frame.config(bg='#D7E3F5')

        # привязываем фрейм к канвасу и настраиваем прокрутку
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        for desk in desks:
            button_desks.append(Button(frame, text=f"{desk[1]}", command=lambda desk=desk: Desk(window, user_interface, desk), **button_style))
            button_desks[desk[0]].config(width=15, height=1)
            button_desks[desk[0]].pack(padx=45, pady=5)

            # обновляем геометрию фрейма и канваса
            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        # задаем размеры кнопок
        button_back.config(width=10, height=1)

        # располагаем кнопки
        button_back.place(relx=0.15, rely=0.05, anchor="center")
        canvas.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.8, anchor='center')
        scrollbar.place(relx=0.8, rely=0.5, relheight=0.8, anchor='center', relwidth=0.05)
    else:
        # создаем кнопки
        button_create = Button(window, text="Создать доску", command=lambda: NewDesk(window, user_interface), **button_style)
        button_back = Button(window, text="Назад", command=lambda: Menu(window, user_interface), **button_style)

        label = Label(window, text="Здесь еще нет досок", bg="#D7E3F5", fg="#043C66", font=("Calibri", 16))

        # задаем размеры кнопок
        button_create.config(width=15, height=1)
        button_back.config(width=10, height=1)

        # располагаем текст и кнопки
        label.place(relx=0.5, rely=0.5, anchor="center")
        button_create.place(relx=0.5, rely=0.7, anchor="center")
        button_back.place(relx=0.15, rely=0.05, anchor="center")

def NewDesk(window, user_interface):

    # функция создания доски
    def try_to_create(desk_name, desk_type):
        deskname = desk_name.get()
        desktype = desk_type.get()
        if messagebox.askyesno(title="Подтвержение операции", message="Создать доску?"):
            if user_interface.create_desk(deskname, desktype):
                messagebox.showinfo('Создание доски', f'Доска {deskname} успешно создана')
                Menu(window, user_interface)
            else:
                messagebox.showerror('Ошибка', 'Доска с таким именем уже существует')
                Menu(window, user_interface)

    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    desk_name=StringVar()

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем стиль для радиокнопок
    radiobutton_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Arial Black", 11), "bd": 0, "activebackground": "#304D63"}

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем текстовые поля
    label_deskname = Label(window, text="Имя доски:", **label_style)
    label_desktype = Label(window, text="Тип:", **label_style)

    # создаем поля для ввода
    entry_deskname = Entry(window, textvariable=desk_name, **entry_style)

    # создаем RadioButton
    desk_type = StringVar()
    rb_personal = Radiobutton(window, text="Личная", variable=desk_type, value=0, **radiobutton_style)
    rb_shared = Radiobutton(window, text="Общая", variable=desk_type, value=1, **radiobutton_style)

    # создаем кнопки
    button_create = Button(window, text="Создать доску", command=lambda: try_to_create(desk_name, desk_type), **button_style)
    button_back = Button(window, text="Назад", command = lambda: Menu(window, user_interface), **button_style)

    # задаем размеры кнопок
    button_create.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем текст, поле для ввода, радиокнопки и кнопки
    label_deskname.place(relx=0.38, rely=0.4, anchor="e")
    entry_deskname.place(relx=0.4, rely=0.4, anchor="w")
    label_desktype.place(relx=0.38, rely=0.5, anchor="e")
    rb_personal.place(relx=0.4, rely=0.5, anchor="w")
    rb_shared.place(relx=0.6, rely=0.5, anchor="w")
    button_create.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def Desk(window, user_interface, desk):

    # функция удаления доски
    def try_to_delete(desk_id):
        if messagebox.askyesno(title="Подтвержение операции", message="Удалить доску?"):
            if user_interface.del_desk(desk_id):
                messagebox.showinfo('Удаление доски', 'Доска успешно удалена')
                Menu(window, user_interface)
            else:
                messagebox.showerror('Ошибка', 'При удалении доски произошла ошибка')

    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()
    if desk[2] == 1:
        desk_type = 'Общественная'
    else:
        desk_type = 'Приватная'

    if user_interface.can_edit_desk(desk[0]):
        # создаем стиль для кнопок и текста
        button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"}
        button_style2 = {"bg": "#92ebd3", "fg": "#000000", "font": ("Calibri", 13), "bd": 0,"activebackground": "#304D63"}
        button_style3 = {"bg": "#902d23", "fg": "#000000", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"}

        # создаем кнопки и текст
        button_back = Button(window, text="Назад", command=lambda: Menu(window, user_interface), **button_style)
        button_deskname = Button(window, text=f"{desk[1]}", command=lambda: RenameDesk(window, user_interface, desk), **button_style2)
        button_rights = Button(window, text="Права доступа", command=lambda: EditRights(window, user_interface, desk), **button_style2)
        button_delete = Button(window, text="Удалить", command=lambda: try_to_delete(desk[0]), **button_style3)
        desk_author = Label(window, text=f"Создал {desk[3]}", bg="#D7E3F5", fg="#043C66", font=("Calibri", 12))
        type = Label(window, text=f"{desk_type}", bg="#D7E3F5", fg="#043C66", font=("Calibri", 12))

        # задаем размеры кнопок
        button_back.config(width=10, height=1)
        button_deskname.config(width=12, height=1)
        button_rights.config(width=12, height=1)

        # располагаем кнопки и текст
        button_back.place(relx=0.05, rely=0.05, anchor="w")
        button_deskname.place(relx=0.5, rely=0.05, anchor="center")
        button_rights.place(relx=0.95, rely=0.05, anchor="e")
        button_delete.place(relx=0.99, rely=0.95, anchor="e")
        type.place(relx=0.15, rely=0.95, anchor="center")
        desk_author.place(relx=0.5, rely=0.95, anchor="center")

def RenameDesk(window, user_interface, desk):

    deskname = StringVar()

    def try_to_rename(desk, deskname):
        new_deskname = deskname.get()  # Получаем значение из поля ввода
        if messagebox.askyesno(title="Подтвержение операции", message="Сменить имя?"):
            if user_interface.change_desk_name(desk[0], new_deskname):
                messagebox.showinfo('Изменение названия доски', f'Название доски успешно изменено на {new_deskname}')
                Desk(window, user_interface, desk)
            else:
                messagebox.showerror('Ошибка', 'Доска с таким именем уже существует')
                Desk(window, user_interface, desk)

    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}
    label_style2 = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Arial Black", 16)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"}

    # создаем кнопки
    button_rename = Button(window, text="Переименовать", command=lambda: try_to_rename(desk, deskname), **button_style)
    button_back = Button(window, text="Назад", command=lambda: Desk(window, user_interface, desk), **button_style)

    # создаем текстовые поля
    label_newdeskname = Label(window, text="Новое имя:", **label_style)
    label_olddeskname = Label(window, text=f"{desk[1]}", **label_style2)

    # создаем поля для ввода
    entry_newdeskname = Entry(window, textvariable=deskname, **entry_style)

    # задаем размеры кнопок
    button_rename.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_rename.place(relx=0.5, rely=0.6, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")
    label_newdeskname.place(relx=0.38, rely=0.5, anchor="e")
    label_olddeskname.place(relx=0.5, rely=0.4, anchor="center")
    entry_newdeskname.place(relx=0.4, rely=0.5, anchor="w")

def EditRights(window, user_interface, desk):
    # получаем список пользователей
    #users = user_interface.get_all_user_with_edit_rights(desk[0])
    users = [(1, 'Bob', 0), (3, 'Sera', 1), (33, 'Pol', 1), (3, 'Sera', 1), (33, 'Pol', 1), (3, 'Sera', 1), (33, 'Pol', 1), (3, 'Sera', 1), (33, 'Pol', 1), (3, 'Sera', 1), (33, 'Pol', 1), (3, 'Sera', 1), (33, 'Pol', 1)]

    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для кнопок и текста
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"}
    button_style2 = {"fg": "#043C66", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"}
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Arial Black", 16)}

    # создаем кнопки и текст
    button_back = Button(window, text="Назад", command=lambda: Desk(window, user_interface, desk), **button_style)
    label_deskname = Label(window, text=f"{desk[1]}", **label_style)

    # создаем контейнер для кнопок с возможностью прокрутки
    canvas = Canvas(window, bg='#D7E3F5')
    scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
    frame = Frame(canvas)
    frame.config(bg='#D7E3F5')

    # привязываем фрейм к канвасу и настраиваем прокрутку
    canvas.create_window((0, 0), window=frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)
    button_users = []

    for user in users:
        if user[2] == 1:
            button = Button(frame, bg='#90cd6b', text=f"{user[1]}", command=lambda user=user: (user_interface.del_edit_rights_on_public_desk(user[1], desk[0]), EditRights(window, user_interface, desk)), **button_style2)
        else:
            button = Button(frame, bg='#cd6b6b', text=f"{user[1]}", command=lambda user=user: (user_interface.add_edit_rights_on_public_desk(user[1], desk[0]), EditRights(window, user_interface, desk)), **button_style2)

        button.config(width=15, height=1)
        button.pack(padx=45, pady=5)
        button_users.append(button)

        # обновляем геометрию фрейма и канваса
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # задаем размеры кнопок
    button_back.config(width=10, height=1)

    # располагаем кнопки и текст
    button_back.place(relx=0.15, rely=0.05, anchor="center")
    label_deskname.place(relx=0.5, rely=0.05, anchor="center")
    canvas.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.8, anchor='center')
    scrollbar.place(relx=0.8, rely=0.5, relheight=0.8, anchor='center', relwidth=0.05)

window = Tk()
window.geometry("450x550")
window.title("TaskManager")
window.config(bg="#D7E3F5")

Start(window)
window.mainloop()
