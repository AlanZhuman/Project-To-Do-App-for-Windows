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

def window_Update():
    tk.update()
    tk.update_idletasks()
    print("Window Updated")

mainframe = ttk.Frame(tk)
mainframe.grid(column=0, row=0, sticky=(NSEW))

for c in range(8): mainframe.columnconfigure(c, weight = 1)
for r in range(8): mainframe.rowconfigure(r, weight = 1)

menu_bg = Canvas(mainframe, bg="black", width='144')
menu_bg.grid(row=0, column=0, rowspan=8, sticky=NSEW)

mainframe.columnconfigure(0, weight = 0)

note_menu_bg = Canvas(mainframe, bg="white")
note_menu_bg.grid(row=0, column=1, rowspan=8,columnspan=7, sticky=NSEW)

note_count = 0
class Note:
    notes_list = []
    def __init__(self, pos_row, pos_col) -> None:
        self.pos_row = pos_row
        self.pos_col = pos_col
        Note.notes_list.append(self)
    
    @classmethod
    def note_calc(self):    #Вычисление координат для новой заметки
        global note_count
        global pos_row
        global pos_col
        note_count = len(Note.notes_list)

        if note_count % 2 == 0:
            pos_row = note_count + (note_count/2)
            pos_col = 3
        elif note_count % 2 != 0:
            pos_row = ((note_count-1)/2)*3
            pos_col = 6 

        note_count += 1
        new_note_cord = (int(pos_row), pos_col)
        return new_note_cord    #Возврат высчитанных координат
    
    def new_position_calc(old_note_pos_index, i_note_pos_index, i_note_pos):
        if i_note_pos_index > old_note_pos_index:
            i_note_pos_index -= 1
            if i_note_pos[1] == 3:
                i_note_pos[0] -= 3
                i_note_pos[1] = 6
            elif i_note_pos[1] == 6:
                i_note_pos[1] = 3
            print (i_note_pos)
            return i_note_pos
        else: pass


    @classmethod
    def createNote(cls, cord):
        Note.notes_list.append([cord[0],cord[1]])
        cls.new_note = Text(mainframe, width='144', border=3, borderwidth=10)
        cls.new_note.grid(row=cord[0], column=cord[1], columnspan=1, rowspan=2, sticky=NS)
        cls.deleteNote_Button(cord, cls.new_note)

    @classmethod
    def deleteNote_Button(cls, cord, note_widget):
        delete_button = Button(cls.new_note, text='x', fg="red", command=lambda: Note.deleteNote(cord, note_widget, delete_button))
        delete_button.grid(row=cord[0], column=cord[1], sticky=NE)
    
    @classmethod
    def deleteNote(cls, instance, note_widget, button_widget):
        instance = list(instance)
        temp_pos = (Note.notes_list.index(instance))
        if instance in Note.notes_list:
            cls.notes_list.pop(Note.notes_list.index(instance))
            for i in Note.notes_list[temp_pos:-1]:
                i = list(i)
                Note.notes_list[Note.notes_list.index(i)] = cls.new_position_calc((Note.notes_list.index(instance)), (Note.notes_list.index(i)) , (i))
            del instance
        note_widget.destroy()
        button_widget.destroy()
        

new_note_button = Button(mainframe, bg='dark green', fg="green", text='+', width="5", height="2", command=lambda: Note.createNote(Note.note_calc()))
new_note_button.grid(row=0, column=0)

tk.mainloop()