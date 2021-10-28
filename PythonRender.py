import tkinter as tk
import VoidPython as VP


class application(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.canvas = tk.Canvas(width=200, height=200)

        self.canvas.create_line(10, 10, 80, 80)

        self.canvas.pack()


def Main():
    root = tk.Tk()
    primApp = application(root)
    primeScene = VP.Scene()
    primeScene.Camera = VP.Camera()
    primeScene.gameObjects.clear()
    cubeObj = VP.gameObject()
    cubeObj.myMesh = VP.CreateCube(10)
    primeScene.addObject(cubeObj)
    VP.Draw(primeScene)

    if False:
        for x in range(0, 1):
            currSet = primeScene.gameObjects[0].myMesh.sets[0]
            currPoints = primeScene.gameObjects[0].myMesh.ProjectedPoints
            primApp.canvas.create_line(currPoints[currSet.x()].x()+100,
                                       currPoints[currSet.x()].y()+100,
                                       currPoints[currSet.y()].x()+100,
                                       currPoints[currSet.y()].y()+100,
                                       currPoints[currSet.z()].x()+100,
                                       currPoints[currSet.z()].y()+100)
    while True:
        primApp.update_idletasks()
        primApp.update()


if __name__ == '__main__':
    Main()
