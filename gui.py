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

    # функция редактирования столбца
    def edit_column(column_id, old_column_name):
        editwindow = Tk()
        editwindow.geometry("450x550")
        editwindow.title("Редактирование столбца")
        editwindow.config(bg="#D7E3F5")
        new_column_name = StringVar()

        # функция подтверждения изменений
        def confirm_changes(column_id, new_column_name):
            new_column_name = new_column_name.get()
            if messagebox.askyesno(title="Подтвержение операции", message="Изменить название столбца?"):
                if user_interface.change_column_name(column_id, new_column_name):
                    messagebox.showinfo('Изменение данных столбца', 'Данные столбца успешно изменены')
                    editwindow.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Во время изменения данных столбца произошла ошибка')
                    editwindow.destroy()

        # функция подтверждения удаления
        def confirm_deletion(column_id):
            if messagebox.askyesno(title="Подтвержение операции", message="Удалить столбец?"):
                if user_interface.change_column_name(column_id, new_column_name):
                    messagebox.showinfo('Удаление столбца', 'Столбец был успешно удален')
                    editwindow.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Во время удаления столбца произошла ошибка')
                    editwindow.destroy()

        # создаем стили
        label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}
        entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}
        button_style = {"fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

        # создаем текстовые поля и кнопки
        label_title = Label(editwindow, text="Название:", **label_style)
        entry_title = Entry(editwindow, textvariable=new_column_name, **entry_style)
        entry_title.insert(0, old_column_name)

        button_confirm = Button(editwindow, text="Подтвердить", command=lambda: (confirm_changes(column_id, new_column_name)), bg='#78e082', **button_style)
        button_cancel = Button(editwindow, text="Отмена", bg='#e07878', command=lambda: editwindow.destroy(), **button_style)
        button_delete = Button(editwindow, text="Удалить столбец", bg='#e07878', command=lambda: (confirm_deletion(column_id), Desk(window, user_interface, desk)), **button_style)

        # задаем размеры кнопок
        button_confirm.config(width=12, height=1)
        button_cancel.config(width=12, height=1)
        button_delete.config(width=24, height=1)

        # располагаем текст, поля для ввода и кнопки
        label_title.place(relx=0.4, rely=0.5, anchor="e")
        entry_title.place(relx=0.42, rely=0.5, anchor="w")
        button_confirm.place(relx=0.7, rely=0.7, anchor="center")
        button_cancel.place(relx=0.3, rely=0.7, anchor="center")
        button_delete.place(relx=0.5, rely=0.8, anchor="center")

    # функция добавления карточки
    def add_card(desk_id, column_id):
        editwindow = Tk()
        editwindow.geometry("450x550")
        editwindow.title("Добавление карточки")
        editwindow.config(bg='#D7E3F5')
        card_status = 1
        # функция смены статуса
        def change_status():
            nonlocal card_status
            if card_status < 3:
                card_status += 1
            else:
                card_status = 1
            button_cardstatus.config(text=f"Статус: {card_status}")

        card_name = StringVar()

        # функция подтверждения изменений
        def confirm_changes(card_name, card_status):
            if user_interface.add_card_to_column(card_name, card_status, desk_id, column_id):
                messagebox.showinfo('Добавление карточки', 'Карточка была успешно добавлена')
                editwindow.destroy()
            else:
                messagebox.showerror('Ошибка', 'Во время добавления карточки произошла ошибка')
                editwindow.destroy()

        # создаем стили
        label_style = {"bg": '#D7E3F5', "fg": "#043C66", "font": ("Calibri", 14)}
        entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}
        button_style = {"fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}
        button_style1 = {"bg": '#D7E3F5', "fg": "#000000", "font": ("Arial Black", 14), "bd": 0,"activebackground": "#304D63"}

        # создаем текстовые поля и кнопки
        label_title = Label(editwindow, text="Название:", **label_style)
        entry_title = Entry(editwindow, textvariable=card_name, **entry_style)
        button_confirm = Button(editwindow, text="Подтвердить",command=lambda: confirm_changes(card_name.get(), card_status), bg='#78e082',**button_style)
        button_cancel = Button(editwindow, text="Отмена", bg='#e07878', command=lambda: editwindow.destroy(),**button_style)
        button_cardstatus = Button(editwindow, text=f"Статус: {card_status}", command=change_status, **button_style1)

        # задаем размеры кнопок
        button_confirm.config(width=15, height=1)
        button_cancel.config(width=10, height=1)
        button_cardstatus.config(width=15, height=1)

        # располагаем текст, поля для ввода и кнопки
        label_title.place(relx=0.38, rely=0.45, anchor="e")
        entry_title.place(relx=0.4, rely=0.45, anchor="w")
        button_confirm.place(relx=0.7, rely=0.8, anchor="center")
        button_cancel.place(relx=0.3, rely=0.8, anchor="center")
        button_cardstatus.place(relx=0.5, rely=0.6, anchor="center")


    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()
    if desk[2] == 1:
        desk_type = 'Общественная'
    else:
        desk_type = 'Приватная'
    columns = user_interface.get_desk_card(desk[0])

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

        # создаем контейнер для столбцов с возможностью прокрутки
        maincanvas = Canvas(window, bg='#D7E3F5')
        mainscrollbar = Scrollbar(window, orient=HORIZONTAL, command=maincanvas.xview)
        mainframe = Frame(maincanvas)
        mainframe.config(bg='#D7E3F5')

        # привязываем фрейм к канвасу и настраиваем прокрутку
        maincanvas.create_window((0, 0), window=mainframe, anchor='nw')
        maincanvas.config(xscrollcommand=mainscrollbar.set)
        i = 0
        for id, title in columns.items():
            # создаем контейнер для кнопок с возможностью прокрутки
            canvas = Canvas(maincanvas, bg='#D7E3F5')
            scrollbar = Scrollbar(maincanvas, orient=VERTICAL, command=canvas.yview)
            frame = Frame(canvas)
            frame.config(bg='#D7E3F5')

            # привязываем фрейм к канвасу и настраиваем прокрутку
            canvas.create_window((0, 0), window=frame, anchor='nw')
            canvas.configure(yscrollcommand=scrollbar.set)
            button_card = []
            button = Button(frame, text=f"{id[1]}", command = lambda: (edit_column(id[0],id[1]), Desk(window, user_interface, desk)), **{"bg": "#D7E3F5", "fg": "#2c2c2c", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"})
            button.config(width=12, height=1)
            button.pack(padx=25, pady=5)
            for card in title:
                button = Button(frame, text=f"{card[1]}", command=lambda card=card: Card(window, user_interface, user_interface.get_full_card_info(card[0]), desk), **button_style2)

                button.config(width=15, height=1)
                button.pack(padx=25, pady=5)
                button_card.append(button)

                # обновляем геометрию фрейма и канваса
                frame.update_idletasks()
                canvas.config(scrollregion=canvas.bbox("all"))

            button = Button(frame, text=f"+ Добавить карточку", command=lambda:(add_card(desk[0],card[0]), Desk(window, user_interface, desk)), **{"bg": "#D7E3F5", "fg": "#2c2c2c", "font": ("Arial", 10), "bd": 0,"activebackground": "#304D63"})
            button.config(width=20, height=2)
            button.pack(padx=25, pady=5)

            # обновляем геометрию фрейма и канваса
            mainframe.update_idletasks()
            maincanvas.config(scrollregion=canvas.bbox("all"))

            canvas.place(relx=i, rely=0.5, relwidth=0.5, relheight=0.99, anchor='w')
            scrollbar.place(relx=0.5 + i, rely=0.5, relheight=1, anchor='center', relwidth=0.05)
            i += 0.525

        maincanvas.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.77, anchor='n')
        mainscrollbar.place(relx=0.5, rely=0.87, relheight=0.03, anchor='n', relwidth=0.9)

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
    users = user_interface.get_all_user_with_edit_rights(desk[0])

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

def Card(window, user_interface, card, desk):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # назначаем цвет фона
    if card['card_status'] == 1:
        background_color='#87e078'
    elif card['card_status'] == 2:
        background_color = '#e0da78'
    elif card['card_status'] == 3:
        background_color = '#e07878'
    else:
        background_color = '#D7E3F5'
    window.config(bg=background_color)

    # функция смены статуса
    def change_status(window, user_interface, card):
        if card['card_status'] < 3:
            card['card_status'] += 1
        else:
            card['card_status'] = 1
        user_interface.change_card_status(card['card_id'], card['card_status'])

    # функция редактирования названия и текста
    def card_edit(card_id, card_name, card_text):
        editwindow = Tk()
        editwindow.geometry("450x550")
        editwindow.title("Редактирование карточки")
        editwindow.config(bg="#D7E3F5")
        new_title=StringVar()
        new_text=StringVar()

        # функция подтверждения изменений
        def confirm_changes(card_id, new_text, new_title):
            newtext = new_text.get()
            newtitle = new_title.get()
            if messagebox.askyesno(title="Подтвержение операции", message="Изменить данные карточки?"):
                if (user_interface.change_card_title(card_id, newtitle) and user_interface.change_card_text(card_id, newtext)):
                    messagebox.showinfo('Изменение данных карточки', 'Данные карточки успешно изменены')
                    editwindow.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Во время изменения данных карточки произошла ошибка')
                    editwindow.destroy()

        # создаем стили
        label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}
        entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}
        button_style = {"fg": "#043C66", "font": ("Arial Black", 12), "bd": 0,"activebackground": "#304D63"}

        # создаем текстовые поля и кнопки
        label_title = Label(editwindow, text="Название:", **label_style)
        label_text = Label(editwindow, text="Текст:", **label_style)
        entry_title = Entry(editwindow, textvariable=new_title, **entry_style)
        entry_title.insert(0, card_name)

        text_widget = Text(editwindow, **entry_style)
        text_widget.place(relx=0.32, rely=0.48, anchor="w", relwidth=0.6, relheight=0.25)
        scrollbar = Scrollbar(editwindow, command=text_widget.yview)
        scrollbar.place(relx=0.92, rely=0.48, relheight=0.25, anchor="center")
        text_widget.config(yscrollcommand=scrollbar.set, padx=5, pady=5)
        text_widget.insert("1.0", card_text)

        button_confirm = Button(editwindow, text="Подтвердить", command=lambda:(confirm_changes(card_id, new_text, new_title)),bg='#78e082', **button_style)
        button_cancel = Button(editwindow, text="Отмена", bg='#e07878', command=lambda: editwindow.destroy(), **button_style)

        # задаем размеры кнопок
        button_confirm.config(width=15, height=1)
        button_cancel.config(width=10, height=1)

        # располагаем текст, поля для ввода и кнопки
        label_title.place(relx=0.3, rely=0.3, anchor="e")
        entry_title.place(relx=0.32, rely=0.3, anchor="w")
        label_text.place(relx=0.3, rely=0.4, anchor="e")
        button_confirm.place(relx=0.7, rely=0.7, anchor="center")
        button_cancel.place(relx=0.3, rely=0.7, anchor="center")

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}
    button_style1 = {"bg": background_color, "fg": "#000000", "font": ("Arial Black", 14), "bd": 0, "activebackground": "#304D63"}
    button_style2 = {"bg": background_color, "fg": "#043C66", "font": ("Arial Regular", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки и текст
    button_back = Button(window, text="Назад", command=lambda: (window.config(bg="#D7E3F5"), Desk(window, user_interface, desk)), **button_style)
    button_cardname = Label(window, text=f"{card['card_title']}", bg=background_color, fg="#043C66", font=("Arial Black", 16))
    button_edittext = Button(window, text = "Изменить название или текст", command=lambda: card_edit(card['card_id'], card['card_title'], card['card_text']), **button_style2)
    button_cardstatus = Button(window, text = f"Статус: {card['card_status']}", command=lambda: (change_status(window, user_interface, card), Card(window, user_interface, card, desk)), **button_style1)
    text = Label(window, text=f"{card['card_text']}", bg=background_color, fg="#000000", font=("Calibri", 14))
    author = Label(window, text=f"Создал {card['card_author_login']}", bg=background_color, fg="#043C66", font=("Calibri", 12))

    # задаем размеры кнопок
    button_back.config(width=10, height=1)
    button_cardname.config(width=15, height=1)
    button_edittext.config(width=25, height=1)
    button_cardstatus.config(width=15, height=1)

    # располагаем кнопки
    button_back.place(relx=0.15, rely=0.05, anchor="center")
    button_cardname.place(relx=0.5, rely=0.3, anchor="center")
    button_edittext.place(relx=0.5, rely=0.65, anchor="center")
    button_cardstatus.place(relx=0.5, rely=0.75, anchor="center")
    text.place(relx=0.5, rely=0.5, anchor="center")
    author.place(relx=0.5, rely=0.95, anchor="center")

login=''
password=''
user_interface = UserInterface(login, password)
desk = (0, 'Доска 1', 0, 'Myself')
window = Tk()
window.geometry("450x550")
window.title("TaskManager")
window.config(bg="#D7E3F5")

Start(window)
window.mainloop()
