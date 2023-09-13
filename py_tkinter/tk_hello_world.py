"""Module for tkinter Hello World"""

from tkinter import *
from tkinter import ttk

class TkUse:
    """Tkinter use"""
    root: Tk
    frm: ttk.Frame
    lbl: ttk.Label
    btn: ttk.Button

    def create_frame(self)-> None:
        """Create frame using tk"""
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

    def create_button(self)-> None:
        """Create button """

        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)

    def create_label(self)-> None:
        """Create label """
        ttk.Label(self.frm, text="Hello World!").grid(column=0, row=0)

    def display(self)-> None:
        """Display frame with button and label """
        self.create_frame()
        self.create_label()
        self.create_button()
        self.root.mainloop()

if __name__ == '__main__':
    tk_use_instance = TkUse()
    tk_use_instance.display()
