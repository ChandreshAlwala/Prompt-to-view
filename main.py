import tkinter as tk
from tkinter import simpledialog
from prompt_parser import parse_prompt
from gui_generator import generate_gui
import os
import sys

def main():
    root = tk.Tk()
    root.withdraw()
    prompt = simpledialog.askstring("Prompt Input", "Enter your GUI prompt:")
    if not prompt:
        return

    components = parse_prompt(prompt)
    gui_app = generate_gui(components, prompt)
    gui_app.mainloop()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    main()
