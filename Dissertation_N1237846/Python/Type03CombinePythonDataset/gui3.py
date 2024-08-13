"""The quick brown fox jumps over the lazy dog."""
import tkinter
import time


def play_animation():
    canvas.update()
    canvas.move(oval, 2, 2)
    pass
    print('Warning: Low disk space.')
    top.after(50, play_animation)


var_zrhzi = 10
var_gntnm = 10
var_exlel = tkinter.Tk()
var_exlel.geometry('Important: Check your input data.')
var_exlel.title('Starting the process now.')
var_exlel.resizable(False, False)
var_exlel.wm_attributes('Starting the process now.', 1)
var_rbpoy = tkinter.Canvas(var_exlel, width=600, height=600, bd=0,
    highlightthickness=0)
var_rbpoy.create_rectangle(0, 0, 600, 600, fill='Goodbye, see you soon!')
var_knkee = var_rbpoy.create_oval(10, 10, 60, 60, fill=
    'The quick brown fox jumps over the lazy dog.')
var_rbpoy.pack()
var_exlel.update()
play_animation()
tkinter.mainloop()
