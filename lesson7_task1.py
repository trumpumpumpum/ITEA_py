from tkinter import *
import time
import os

time = str(time.localtime())


def save_file():
    firstname_inf = firstname.get()
    lastname_inf = lastname.get()
    phone_inf = phone.get()
    address_inf = address.get()
    time_inf = time

    file = open(r'C:\Users\Igor\PycharmProjects\untitled2\lesson7\my_contacts.txt', 'a', encoding='utf-8')
    file.write(firstname_inf + '\n')
    file.write(lastname_inf + '\n')
    file.write(phone_inf + '\n')
    file.write(address_inf + '\n')
    file.write(time_inf + '\n')
    file.write('\n')
    file.close()

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)


screen = Tk()
screen.geometry('600x400')
screen.title('Записная книга')


def opn():
    root1 = Tk()
    root1.geometry('600x400')
    root1.title('Мои контакты')
    listbox = Listbox(root1, height=600, width=400)
    listbox.insert(END, 'Список сохраненных контактов:')
    with open('my_contacts.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
    for i in lst:
        listbox.insert(END, i)
    def cls_clear():
        open(r'C:\Users\Igor\PycharmProjects\untitled2\lesson7\my_contacts.txt', 'w', encoding='utf-8').close()
        root1.destroy()

    clear_btn = Button(root1, text='Очистить список', fg='Black', bg='green', command=cls_clear)
    clear_btn.pack()
    listbox.pack()
    root1.mainloop()


firstname_text = Label(text='Имя ')
lastname_text = Label(text='Фамилия ')
phone_text = Label(text='Номер телефона ')
address_text = Label(text='Адрес ')

firstname_text.place(x=15, y=70)
lastname_text.place(x=15, y=140)
phone_text.place(x=15, y=210)
address_text.place(x=15, y=280)

firstname = StringVar()
lastname = StringVar()
phone = StringVar()
address = StringVar()

firstname_entry = Entry(textvariable=firstname, width='30')
lastname_entry = Entry(textvariable=lastname, width='30')
phone_entry = Entry(textvariable=phone, width='30')
address_entry = Entry(textvariable=address, width='30')

firstname_entry.place(x=15, y=100)
lastname_entry.place(x=15, y=170)
phone_entry.place(x=15, y=240)
address_entry.place(x=15, y=310)

my_contacts_btn = Button(screen,
                         text='Мои контакты',
                         fg='Black',
                         bg='green',
                         command=opn)

save_btn = Button(screen,
                  text='Сохранить',
                  fg='Black',
                  bg='green',
                  command=save_file)

save_btn.pack()
my_contacts_btn.pack()

screen.mainloop()