import tkinter as tk
from Math3D import Vec4, RotateY
import VoidPython as VP
import keyboard


class application(tk.Frame):

    windowOpen = True

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.canvas = tk.Canvas(width=200, height=200)

        self.canvas.pack()

    def onWindowClose(self):
        self.windowOpen = False


def Main():

    # Setup app
    root = tk.Tk()
    primApp = application(root)
    root.protocol("WM_DELETE_WINDOW", primApp.onWindowClose)
    primeScene = VP.Scene()
    primeScene.Camera = VP.Camera(position=Vec4(0, 0, 5, 1))
    primeScene.gameObjects.clear()
    cubeObj = VP.gameObject()
    cubeObj.myMesh = VP.CreateCube()
    RotateY(cubeObj.transform.Matrix, 15.0)
    primeScene.addObject(cubeObj)

    # Setup inputs
    keyboard.on_press_key("w", primeScene.MoveCameraNegZ)
    keyboard.on_press_key("s", primeScene.MoveCameraPosZ)
    keyboard.on_press_key("a", primeScene.MoveCameraPosX)
    keyboard.on_press_key("d", primeScene.MoveCameraNegX)
    keyboard.on_press_key("q", primeScene.MoveCameraPosY)
    keyboard.on_press_key("e", primeScene.MoveCameraNegY)

    while primApp.windowOpen:
        if VP.Draw(primeScene):
            primApp.canvas.delete('all')

            for obj in primeScene.gameObjects:
                currPoints = obj.myMesh.ProjectedPoints
                for set in obj.myMesh.sets:
                    primApp.canvas.create_line(
                                    currPoints[set[0]].x()*100+100, currPoints[set[0]].y()*100+100,
                                    currPoints[set[1]].x()*100+100, currPoints[set[1]].y()*100+100,
                                    currPoints[set[2]].x()*100+100, currPoints[set[2]].y()*100+100,
                                    currPoints[set[0]].x()*100+100, currPoints[set[0]].y()*100+100)
        primApp.update_idletasks()
        primApp.update()

    primApp.master.destroy()


if __name__ == '__main__':
    Main()
