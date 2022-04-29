from __future__ import annotations
from cmath import tan
from math import radians
from keyboard import on_press_key as onKeyPress
import Math3D

class Mesh():
    def __init__(self):
        self.points = [Math3D.Vec4()]
        self.ProjectedPoints = self.points
        self.sets = [Math3D.Vec3()]


class Transform():
    def __init__(self, parent=None):
        self.parent = parent
        self.Matrix = Math3D.Mat4x4()
        self.Position = Math3D.Vec4()
        self.Rotation = Math3D.Vec4()


class Camera:
    def __init__(self, position=Math3D.Vec4(),
                 nearPlane=1, farPlane=10) -> None:
        self.transform = None
        self.near = nearPlane
        self.far = farPlane
        self.target = Math3D.Vec4
        self.position = position
        self.up = Math3D.Vec4(0, 1)
        self.right = Math3D.Vec4(1)

    def MovePosX(self):
        self.position = self.position + Math3D.Vec4(x=1)

    def MoveNegX(self):
        self.position = self.position + Math3D.Vec4(x=-1)

    def MovePosY(self):
        self.position = self.position + Math3D.Vec4(y=1)

    def MoveNegY(self):
        self.position = self.position + Math3D.Vec4(y=-1)

    def MovePosZ(self):
        self.position = self.position + Math3D.Vec4(z=1)

    def MoveNegZ(self):
        self.position = self.position + Math3D.Vec4(z=-1)

    def createLookat(self, target: Math3D.Vec4 = Math3D.Vec4(0,0,1,0)) -> Math3D.Mat4x4:
        target = self.position + Math3D.Vec4(x=1)
        zAxis = Math3D.normalize(self.position - target)
        xAxis = Math3D.normalize(Math3D.cross(self.up,zAxis))
        yAxis = Math3D.cross(zAxis,xAxis)

        orientation = Math3D.Mat4x4(array=[
                                           Math3D.Vec4(xAxis.x(), yAxis.x(), zAxis.x(), 0),
                                           Math3D.Vec4(xAxis.y(), yAxis.y(), zAxis.y(), 0),
                                           Math3D.Vec4(xAxis.z(), yAxis.z(), zAxis.z(), 0),
                                           Math3D.Vec4(w=1)
                                          ])

        positionMat = Math3D.Mat4x4()
        positionMat.matrix[3] = (Math3D.Vec4(-self.position.x(), -self.position.y(), -self.position.z(), 1))

        return (orientation*positionMat)

    def createProjMat(self, fov : int = 90) -> Math3D.Mat4x4:
        scale = fov/2
        scale = radians(scale)
        scale = 1/tan(scale).real
        extraVal1 = (self.far/(self.far - self.near))
        extraVal2 = ((self.far*self.near)/(self.far-self.near))
        output = Math3D.Mat4x4(array=[Math3D.Vec4(scale, 0, 0, 0),
                                      Math3D.Vec4(0, scale, 0, 0),
                                      Math3D.Vec4(0, 0, extraVal1, -1),
                                      Math3D.Vec4(0, 0, extraVal2, 0)])

        return output


class gameObject:
    def __init__(self) -> None:
        self.myMesh = Mesh()
        self.transform = Math3D.Mat4x4()

    def updateMesh(self) -> None:
        for point in self.myMesh.points:
            point = self.transform * point
        return


class Scene:
    def __init__(self) -> None:
        self.gameObjects = [gameObject()]
        self.Camera = Camera()
        self.Refresh = True

    def addObject(self, obj: gameObject):
        if not isinstance(obj, gameObject):
            return
        self.gameObjects.append(obj)

    def MoveCameraPosX(self, other):
        self.Camera.MovePosX()
        self.Refresh = True

    def MoveCameraNegX(self, other):
        self.Camera.MoveNegX()
        self.Refresh = True

    def MoveCameraPosY(self, other):
        self.Camera.MovePosY()
        self.Refresh = True

    def MoveCameraNegY(self, other):
        self.Camera.MoveNegY()
        self.Refresh = True

    def MoveCameraPosZ(self, other):
        self.Camera.MovePosZ()
        self.Refresh = True

    def MoveCameraNegZ(self, other):
        self.Camera.MoveNegZ()
        self.Refresh = True


def CreateCube(scale=1) -> Mesh:
    if scale == 0:
        scale = 1
    elif scale < 0:
        scale = abs(scale)

    output = Mesh()
    output.points = [Math3D.Vec4(1*scale,   1*scale,    1*scale,   0),
                     Math3D.Vec4(1*scale,   1*scale,   -1*scale,   0),
                     Math3D.Vec4(-1*scale,  1*scale,   -1*scale,   0),
                     Math3D.Vec4(-1*scale,  1*scale,    1*scale,   0),
                     Math3D.Vec4(1*scale,  -1*scale,    1*scale,   0),
                     Math3D.Vec4(1*scale,  -1*scale,   -1*scale,   0),
                     Math3D.Vec4(-1*scale, -1*scale,   -1*scale,   0),
                     Math3D.Vec4(-1*scale, -1*scale,    1*scale,   0)]

    output.sets = [Math3D.Vec3(6, 2, 1),
                   Math3D.Vec3(6, 1, 5),
                   Math3D.Vec3(5, 1, 0),
                   Math3D.Vec3(5, 0, 4),
                   Math3D.Vec3(4, 0, 3),
                   Math3D.Vec3(4, 3, 7),
                   Math3D.Vec3(7, 3, 2),
                   Math3D.Vec3(7, 2, 6),
                   Math3D.Vec3(2, 3, 0),
                   Math3D.Vec3(2, 0, 1),
                   Math3D.Vec3(7, 6, 5),
                   Math3D.Vec3(7, 5, 4)]

    return output


def Draw(scene: Scene) -> bool:

    if(len(scene.gameObjects) <= 0 or not scene.Refresh):
        return False

    projMat = Math3D.lookAt()
    for gObj in scene.gameObjects:
        gObj.myMesh.ProjectedPoints.clear()
        FinalMat = gObj.transform
        FinalMat = FinalMat*scene.Camera.createLookat()
        FinalMat = FinalMat*scene.Camera.createProjMat()
        for point in gObj.myMesh.points:
            gObj.myMesh.ProjectedPoints.append(point*FinalMat)

    scene.Refresh = False
    return True