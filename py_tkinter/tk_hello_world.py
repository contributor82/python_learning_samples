"""Module for tkinter Hello World"""

# from tkinter import * #type: ignore
from tkinter import Tk, ttk, HORIZONTAL

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
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=36, row=0)

    def create_label(self)-> None:
        """Create label """
        ttk.Label(self.frm, text="Hello World!").grid(column=0, row=0)

    def create_textbox(self)-> None:
        """Create textbox"""
        ttk.Entry(self.frm, width=20).grid(column=14, row=0)

    def create_checkbutton(self)-> None:
        """Create checkbutton"""
        ttk.Checkbutton(self.frm, text="Checkbutton").grid(column=15, row=0)

    def create_line(self)-> None:
        """Create line"""
        ttk.Separator(self.frm, orient=HORIZONTAL).grid(column=0,
                                                        row=5,
                                                        columnspan=37,
                                                        sticky='WE')

    def display(self)-> None:
        """Display frame with button and label """
        self.create_frame()
        self.create_label()
        self.create_textbox()
        self.create_button()
        self.create_line()
        self.root.mainloop()

if __name__ == '__main__':
    tk_use_instance = TkUse()
    tk_use_instance.display()
