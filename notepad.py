import tkinter
import os

from tkinter import ttk
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title='Выберите файл:',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


# новый файл/пустое поле
def new_file():
    editor.delete(1.0, 'end')


# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding='utf-8') as file:
            text = file.read()
            editor.delete(1.0, 'end')
            editor.insert(1.0, text)


# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension='.txt')
    if filepath != "":
        text = editor.get(1.0, 'end')
        with open(filepath, "w", encoding='utf-8') as file:
            file.write(text)


def close_window():
    window.destroy()
global about_program_window
def about_program():
    global about_program_window
    about_program_window = tkinter.Tk()
    about_program_window.title('О программе')
    about_program_window.geometry('250x250')
    about_program_window.configure(bg='white')
    about_program_window.resizable(False, False)
    label = ttk.Label(about_program_window, text="О Программе:\nРазработчик: Фомина Надежда.\nВерсия: 1.0", background='white')
    label.pack(anchor='center', expand=1)
    button_close = tkinter.Button(about_program_window, height=1, width=10,
                                  text='Закрыть', command=about_program_window_close)
    button_close.pack(anchor='center', side = 'bottom', pady=20)

def about_program_window_close():
    about_program_window.destroy()

def how_to_use_notepad():
    with open('how_to.txt', "r", encoding='utf-8') as file:
        text = file.read()
        editor.delete(1.0, 'end')
        editor.insert(1.0, text)

window = tkinter.Tk()
window.title('Блокнот')
window.geometry('600x300')
window.configure(bg='grey')
window.resizable(False, False)

main_menu = tkinter.Menu()
file_menu = tkinter.Menu(tearoff=0)

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Инфо", command=how_to_use_notepad)
main_menu.add_cascade(label="О программе", command=about_program)

window.config(menu=main_menu)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=close_window)

txt_frm = tkinter.Frame(window, width=600, height=300)
txt_frm.grid(row=0, column=0)
txt_frm.grid_propagate(False)
txt_frm.grid_rowconfigure(0, weight=1)
txt_frm.grid_columnconfigure(0, weight=1)
editor = tkinter.Text(txt_frm, borderwidth=3)
editor.pack(expand=1)
editor.grid(column=0, columnspan=2, row=0, sticky="nsew", padx=1, pady=1)

# txt = tkinte.Text(txt_frm, borderwidth=3, relief="sunken")
# txt.config(font=("consolas", 12), undo=True, wrap=NONE)
# txt.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)

scrollb = tkinter.Scrollbar(txt_frm, orient="horizontal", command=editor.xview)
scrollb.grid(row=1, column=0, sticky='nsew')
editor['xscrollcommand'] = scrollb.set

scrollby = tkinter.Scrollbar(txt_frm, orient="vertical", command=editor.yview)
scrollby.grid(row=0, column=1, sticky='nsew')
editor['yscrollcommand'] = scrollby.set

# text = tkinter.Label(window, text = 'Файл:', height=2, width=50, background='silver')
# text.grid(column = 1, row = 1)
# button_select = tkinter.Button(window, height=2, width=50, text='Выбрать файл:',
#                                command=file_select)
# button_select.grid(column = 1, row = 2)
window.mainloop()
