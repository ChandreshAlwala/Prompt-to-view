import tkinter as tk

root = tk.Tk()
root.title('Exported GUI from prompt: Create a contact card')

tk.Label(root, text='Name').grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)
tk.Label(root, text='Phone').grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=3, column=1, padx=5, pady=5)
tk.Label(root, text='Email').grid(row=4, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text='Save Contact').grid(row=6, columnspan=2, pady=10)

root.mainloop()