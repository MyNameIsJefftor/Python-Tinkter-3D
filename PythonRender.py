import tkinter as tk
import VoidPython as Renderer


class application():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('VoidPythonGraphics')
        self.image = tk.Canvas(self.window, width=250, height=250)
        self.screen = Renderer.screen(width=250, height=250)


class app(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.canvas = tk.Canvas(width=200, height=200)
        self.cam = Renderer.Camera(width=200, height=200, distance=6)
        self.objects = list()

        self.draw()
        self.canvas.pack()
        self.pack()

    __slots__ = ["cam", "objects"]

    def draw(self) -> None:
        self.canvas.delete("all")
        if self.objects.__len__ == 0:
            return
        for obj in self.objects:
            for pair in obj.pairs:
                self.canvas.create_polygon(obj.flatPoints[pair[0]],
                                           obj.flatPoints[pair[1]],
                                           obj.flatPoints[pair[2]],
                                           fill="", outline="black")


def Main():
    root = tk.Tk()
    primApp = app(master=root)

    newObject = Renderer.Object()
    newObject.flatPoints = [[25, 25], [50, 25], [50, 50], [75, 75], [50, 75]]
    newObject.pairs = [[0, 1, 2], [2, 3, 4]]

    thirdObject = Renderer.Object()
    thirdObject.points = [[25, 25, 25], [25, 25, -25],
                          [-25, 25, -25], [-25, 25, 25],
                          [25, -25, 25], [25, -25, -25],
                          [-25, -25, -25], [-25, -25, 25]]
    thirdObject.pairs = [[1, 0, 3], [1, 2, 3]]
    # primApp.objects.append(newObject)
    primApp.objects.append(thirdObject)
    while True:
        primApp.update_idletasks()
        primApp.update()
        primApp.draw(xoffset=45)


if __name__ == '__main__':
    Main()
