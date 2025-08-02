import tkinter as tk
from tkinter import messagebox, simpledialog
from reward_system import evaluate_layout, save_to_log
from export_utils import export_gui_to_py
import json

def generate_gui(components, prompt):
    root = tk.Tk()
    root.title("Prompt2View GUI")

    layout_method = tk.StringVar(value="grid")
    entries = {}

    # ✅ Create a dedicated Frame for dynamic widgets
    gui_frame = tk.Frame(root)
    gui_frame.pack(padx=10, pady=10)

    def build_layout(method):
        # Clear the frame only (not the entire root)
        for widget in gui_frame.winfo_children():
            widget.destroy()

        row = 0
        for comp in components:
            try:
                type_, label = comp.split(":")
            except ValueError:
                continue

            widget = None
            if type_ == "label":
                widget = tk.Label(gui_frame, text=label)
            elif type_ == "entry":
                widget = tk.Entry(gui_frame)
                entries[label.lower()] = widget
            elif type_ == "button":
                if label.lower() == "calculate total":
                    def calculate():
                        total = 0
                        for key, entry in entries.items():
                            try:
                                total += float(entry.get())
                            except ValueError:
                                continue
                        messagebox.showinfo("Total", f"Total: ₹{total}")
                    widget = tk.Button(gui_frame, text=label, command=calculate)

                elif label.lower() == "save contact":
                    def save_contact():
                        contact = {k: e.get() for k, e in entries.items()}
                        with open("contacts.json", "a") as f:
                            f.write(json.dumps(contact) + "\\n")
                        messagebox.showinfo("Saved", "Contact saved.")
                    widget = tk.Button(gui_frame, text=label, command=save_contact)

                else:
                    widget = tk.Button(gui_frame, text=label, command=lambda: print(f"{label} clicked"))

            # Use grid or pack inside the frame only
            if method == "grid":
                if type_ == "label":
                    widget.grid(row=row, column=0, sticky="w", padx=5, pady=5)
                elif type_ == "entry":
                    widget.grid(row=row, column=1, padx=5, pady=5)
                    row += 1
                elif type_ == "button":
                    widget.grid(row=row, columnspan=2, pady=10)
                    row += 1
            elif method == "pack":
                widget.pack(anchor="w", padx=10, pady=5)

    def toggle_layout():
        new_method = "pack" if layout_method.get() == "grid" else "grid"
        layout_method.set(new_method)
        build_layout(new_method)

    def export_gui():
        export_gui_to_py(prompt, components)
        messagebox.showinfo("Exported", "GUI exported to 'exported_gui.py'")

    # Build GUI layout
    build_layout(layout_method.get())

    # ✅ These control buttons stay in root window (outside gui_frame)
    tk.Button(root, text="Try New Layout", command=toggle_layout).pack(pady=5)
    tk.Button(root, text="Export GUI to .py", command=export_gui).pack(pady=5)

    # Reward score + save
    score = evaluate_layout(prompt, components)

# ⭐ Ask user for feedback rating (1 to 5)
    try:
        rating = simpledialog.askinteger("Feedback", "Rate this layout (1 to 5):", minvalue=1, maxvalue=5)
    except:
        rating = None

    save_to_log(prompt, components, score, rating=rating)


    return root
