import tkinter as tk
from Math3D import RotateX, RotateY, Vec4
import VoidPython as VP

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
    primeScene.Camera = VP.Camera(position=Vec4(0,0,-5))
    primeScene.gameObjects.clear()
    cubeObj = VP.gameObject()
    cubeObj.myMesh = VP.CreateCube(1)
    #RotateX(cubeObj.transform, 45.0)
    primeScene.addObject(cubeObj)

    # Setup inputs
    VP.onKeyPress("w", primeScene.MoveCameraPosX)
    VP.onKeyPress("s", primeScene.MoveCameraNegX)
    VP.onKeyPress("a", primeScene.MoveCameraPosY)
    VP.onKeyPress("d", primeScene.MoveCameraNegY)
    VP.onKeyPress("q", primeScene.MoveCameraPosZ)
    VP.onKeyPress("e", primeScene.MoveCameraNegZ)

    if False:
        for x in range(0, 1):
            currSet = primeScene.gameObjects[0].myMesh.sets[0]
            currPoints = primeScene.gameObjects[0].myMesh.ProjectedPoints
            primApp.canvas.create_line(currPoints[currSet[0]].x()+50, currPoints[currSet[0]].y()+50,
                                       currPoints[currSet[1]].x()+50, currPoints[currSet[1]].y()+50,
                                       currPoints[currSet[2]].x()+50, currPoints[currSet[2]].y()+50,
                                       currPoints[currSet[0]].x()+50, currPoints[currSet[0]].y()+50,)
    while primApp.windowOpen:
        if VP.Draw(primeScene):
            primApp.canvas.delete('all')

            for obj in primeScene.gameObjects:
               currPoints = primeScene.gameObjects[0].myMesh.ProjectedPoints
               for set in obj.myMesh.sets:
                   primApp.canvas.create_line(currPoints[set[0]].x(), currPoints[set[0]].y(),
                                              currPoints[set[1]].x(), currPoints[set[1]].y(),
                                              currPoints[set[2]].x(), currPoints[set[2]].y(),
                                              currPoints[set[0]].x(), currPoints[set[0]].y(),)
        primApp.update_idletasks()
        primApp.update()

    primApp.master.destroy()

if __name__ == '__main__':
    Main()
