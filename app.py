import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(expand=True, fill='both')
        self.create_menu()
        
    # adding commands under file label
    
    def create_menu(self):
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

    def new_file(self):
        self.textarea.delete('1.0', tk.END)
    
    # Opening file
    
    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                self.textarea.delete('1.0', tk.END)
                self.textarea.insert('1.0', file.read())

    # Sabve File      
                
    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            with open(filepath, 'w') as file:
                file.write(self.textarea.get('1.0', tk.END))

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
