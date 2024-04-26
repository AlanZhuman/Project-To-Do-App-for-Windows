#Main file for app
from tkinter import *
from tkinter import ttk

tk = Tk()
tk.minsize(150,100)
tk.geometry("1024x1440")
tk.title("To-Do & Stuff")

tk.attributes("-fullscreen", False)
tk.bind("<F11>", lambda event: tk.attributes("-fullscreen", not tk.attributes("-fullscreen")))
tk.bind("<Escape>", lambda event: tk.attributes("-fullscreen", False))

tk.columnconfigure(0, weight=1)
tk.rowconfigure(0, weight=1)

mainframe = ttk.Frame(tk)
mainframe.grid(column=0, row=0, sticky=(NSEW))

for c in range(8): mainframe.columnconfigure(c, weight = 1)
for r in range(8): mainframe.rowconfigure(r, weight = 1)

menu_bg = Canvas(mainframe, bg="black", width='144')
menu_bg.grid(row=0, column=0, rowspan=8, sticky=NSEW)

mainframe.columnconfigure(0, weight = 0)

note_menu_bg = Canvas(mainframe, bg="red")
note_menu_bg.grid(row=0, column=1, rowspan=8,columnspan=7, sticky=NSEW)

note_count = 0
pos_row = 0
pos_col = 3
class Note:
    def __init__(self, pos_row, pos_col) -> None:
        self.pos_row = pos_row
        self.pos_col = pos_col
    
    @classmethod
    def note_calc(self):
        global note_count
        global pos_row
        global pos_col
        pos_row_loc = pos_row
        pos_col_loc = pos_col

        if note_count % 2 != 0:
            if pos_col_loc == pos_col:
                pos_col_loc += 3

        elif note_count % 2 == 0:
            pos_row_loc += 3
            if pos_col_loc == 6:
                pos_col_loc -= 3

        pos_row = pos_row_loc
        pos_col = pos_col_loc

        note_count += 1
        new_note_cord = (pos_row, pos_col)
        return new_note_cord

    @classmethod
    def note_del_calc(cls):
        global note_count
        global pos_col
        global pos_row
        
        pos_row_loc = pos_row
        pos_col_loc = pos_col

        if note_count % 2 != 0:
            if note_count == 1:
                pass
            elif pos_col_loc == 3:
                pos_col_loc += 3
                pos_row_loc -= 3

        elif note_count % 2 == 0:
            pos_row_loc -= 3

        pos_row = pos_row_loc
        pos_col = pos_col_loc
        note_count -= 1

        return pos_row, pos_col


    @classmethod
    def deleteNote_Button(cls, note_widget, delete_button, notes_list):
        note_widget.destroy()
        delete_button.destroy()
        print("Note deleted!")

        # Удаляем информацию о заметке из списка заметок
        for note_info in notes_list:
            if note_info[0] == note_widget:
                removed_note_index = notes_list.index(note_info)
                notes_list.remove(note_info)
                break

        # Обновляем расположение оставшихся заметок
        for i in range(removed_note_index, len(notes_list)):
            note = notes_list[i][0]
            row, col = notes_list[i][1]

            # Обновляем координаты только для заметок, следующих за удаленной заметкой
            new_row = row - 2
            note.grid(row=new_row, column=col)
            notes_list[i] = (note, (new_row, col))

    @classmethod
    def createNote_Button(cls, cord, notes_list):
        new_note = Text(mainframe, width=1, height=1)
        new_note.grid(row=cord[0], column=cord[1], columnspan=1, rowspan=2, sticky=NSEW)
        delete_button = Button(mainframe, text='x', fg='red', command=lambda: cls.deleteNote_Button(new_note, delete_button, notes_list))
        delete_button.grid(row=cord[0] + 1, column=cord[1], sticky=EW)
        print("New Note created!")
        notes_list.append((new_note, cord))

notes_list = []

new_note_button = Button(mainframe, text='+', command=lambda: Note.createNote_Button(Note.note_calc(), notes_list))
new_note_button.grid(row=0, column=0, sticky=EW)

new_note_button = Button(mainframe, text='x', fg='red',command=lambda: Note.deleteNote_Button())
new_note_button.grid(row=1, column=0, sticky=EW)


'''
note1 = Canvas(mainframe, bg="grey")
note1.grid(row=0, rowspan=2, column=3, columnspan=1, sticky=EW)

note2 = Canvas(mainframe, bg="grey")
note2.grid(row=0, rowspan=2, column=6, columnspan=1, sticky=EW)
'''

tk.mainloop()