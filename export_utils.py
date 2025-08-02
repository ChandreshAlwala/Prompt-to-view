def export_gui_to_py(prompt, components, filename="exported_gui.py"):
    with open(filename, "w") as f:
        f.write("import tkinter as tk\n\n")
        f.write("root = tk.Tk()\n")
        f.write(f"root.title('Exported GUI from prompt: {prompt}')\n\n")
        row = 0
        for comp in components:
            type_, label = comp.split(":")
            if type_ == "label":
                f.write(f"tk.Label(root, text='{label}').grid(row={row}, column=0, padx=5, pady=5)\n")
            elif type_ == "entry":
                f.write(f"tk.Entry(root).grid(row={row}, column=1, padx=5, pady=5)\n")
            elif type_ == "button":
                f.write(f"tk.Button(root, text='{label}').grid(row={row}, columnspan=2, pady=10)\n")
            row += 1
        f.write("\nroot.mainloop()")
