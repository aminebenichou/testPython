import tkinter as tk
import dbfile as db

db.initialize("todolist.db")
db.createTable("Todo", "(Title text, Description text, Status text)")
db.insertValues("Todo", "('test Title', 'description test', 'pending' )")


window = tk.Tk()

window.geometry("500x300")


frame = tk.Frame()

frame.pack()

title = tk.Label(master=frame, text="hello")
title.pack()


frame1 = tk.Frame(master=window, width=500, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=500)
frame2.pack(fill=tk.Y, side=tk.LEFT, expand=True)


# Textfields
todo_title_label = tk.Label(master=frame2,text="Title", pady=10)
todo_title_label.pack()
todo_title = tk.Entry(master=frame2, width=80) 
todo_title.pack()
todo_description_label = tk.Label(master=frame2,text="Description", pady=10)
todo_description_label.pack()
todo_description = tk.Text(master=frame2, width= 60,)
todo_description.pack()


#buttons

clear_btn = tk.Button




window.mainloop()