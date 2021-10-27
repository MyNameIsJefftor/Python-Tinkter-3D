import tkinter as tk


class application(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.canvas = tk.Canvas(width=200, height=200)

        self.canvas.create_line(10, 10, 80, 80)

        self.canvas.pack()


def Main():
    root = tk.Tk()
    primApp = application(root)
    while True:
        primApp.update_idletasks()
        primApp.update()


if __name__ == '__main__':
    Main()
