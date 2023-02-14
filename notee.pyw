import tkinter as tk
import os

def add_note():
    note = note_entry.get()
    if len(note) > 30:
        note = note[:30]
    notes_list.insert(tk.END, note)
    save_notes()
    note_entry.delete(0, tk.END)

def delete_note():
    selected_index = notes_list.curselection()
    if selected_index:
        notes_list.delete(selected_index)
        save_notes()

def save_notes():
    with open("notes.txt", "w") as f:
        notes = [notes_list.get(index) for index in range(notes_list.size())]
        f.write("\n".join(notes))

def load_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as f:
            for line in f:
                notes_list.insert(tk.END, line.strip())

root = tk.Tk()
root.title("NoTee")
root.geometry("300x600")
root.geometry("+"+str(root.winfo_screenwidth()-300)+"+0")

note_entry = tk.Entry(root)
note_entry.pack(pady=10)

add_button = tk.Button(root, text="Add", command=add_note)
add_button.pack()

delete_button = tk.Button(root, text="Delete", bg='green', fg='white', command=delete_note)
delete_button.pack()

notes_list = tk.Listbox(root, selectmode=tk.BROWSE, highlightthickness=0)
notes_list.pack(fill="both", expand=True)

load_notes()

root.mainloop()
