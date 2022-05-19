from __future__ import annotations
from cmath import tan
from math import radians
import Math3D


class Mesh():
    def __init__(self):
        self.points = [Math3D.Vec4()]
        self.ProjectedPoints = self.points
        self.sets = [Math3D.Vec3()]


class Transform():
    def __init__(self, parent=None):
        self.parent = parent
        self.Matrix = Math3D.Mat4x4(array=[Math3D.Vec4(1, 0, 0, 0),
                                           Math3D.Vec4(0, 1, 0, 0),
                                           Math3D.Vec4(0, 0, 1, 0),
                                           Math3D.Vec4(0, 0, 0, 1)])

    def Translate(self, vec: Math3D.Vec4) -> None:
        self.Matrix[3] += vec

    def Position(self) -> Math3D.Vec4:
        return self.Matrix[3]


class Camera:
    def __init__(self, position=Math3D.Vec4(),
                 nearPlane=1, farPlane=10) -> None:

        trans = Transform()
        trans.Position = position
        trans.Matrix = Math3D.Mat4x4()
        trans.Matrix[3] = position
        self.transform = trans
        self.near = nearPlane
        self.far = farPlane

    def MovePosX(self):
        self.transform.Matrix[3] += Math3D.Vec4(x=0.1)

    def MoveNegX(self):
        self.transform.Matrix[3] += Math3D.Vec4(x=-0.1)

    def MovePosY(self):
        self.transform.Matrix[3] += Math3D.Vec4(y=0.1)

    def MoveNegY(self):
        self.transform.Matrix[3] += Math3D.Vec4(y=-0.1)

    def MovePosZ(self):
        self.transform.Matrix[3] += Math3D.Vec4(z=0.1)

    def MoveNegZ(self):
        self.transform.Matrix[3] += Math3D.Vec4(z=-0.1)

    def createLookat(self,
                     target: Math3D.Vec4 = Math3D.Vec4(0, 0, 1, 0)) -> Math3D.Mat4x4:
        # Look
        zAxis = (self.transform.Position - target).normalize()

        # Right
        xAxis = (Math3D.cross(Math3D.Vec4(0, 1, 0, 0), zAxis)).normalize()

        # Up
        yAxis = Math3D.Vec4(0, 1, 0, 0)

        output = Math3D.Mat4x4(array=[
                                      Math3D.Vec4(xAxis.x(), yAxis.x(), zAxis.x(), 0),
                                      Math3D.Vec4(xAxis.y(), yAxis.y(), zAxis.y(), 0),
                                      Math3D.Vec4(xAxis.z(), yAxis.z(), zAxis.z(), 0),
                                      Math3D.Vec4(Math3D.dot(xAxis, self.transform.Position),
                                                  Math3D.dot(yAxis, self.transform.Position),
                                                  Math3D.dot(zAxis, self.transform.Position),
                                                  1)])

        return (output)

    def createProjMat(self, fov: int = 90, aspectRatio: float = 1.0) -> Math3D.Mat4x4:
        yScale = fov/2
        yScale = radians(yScale)
        yScale = 1/tan(yScale).real
        xScale = yScale * aspectRatio
        extraVal1 = (self.far/(self.far - self.near))
        extraVal2 = ((self.far*self.near)/(self.far-self.near))
        output = Math3D.Mat4x4(array=[Math3D.Vec4(xScale, 0, 0, 0),
                                      Math3D.Vec4(0, yScale, 0, 0),
                                      Math3D.Vec4(0, 0, extraVal1, 1),
                                      Math3D.Vec4(0, 0, extraVal2, 0)])

        return output


class gameObject:
    def __init__(self) -> None:
        self.myMesh = Mesh()
        self.transform = Transform()


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
    output.points = [Math3D.Vec4(1*scale,   1*scale,    1*scale,   1),
                     Math3D.Vec4(1*scale,   1*scale,   -1*scale,   1),
                     Math3D.Vec4(-1*scale,  1*scale,   -1*scale,   1),
                     Math3D.Vec4(-1*scale,  1*scale,    1*scale,   1),
                     Math3D.Vec4(1*scale,  -1*scale,    1*scale,   1),
                     Math3D.Vec4(1*scale,  -1*scale,   -1*scale,   1),
                     Math3D.Vec4(-1*scale, -1*scale,   -1*scale,   1),
                     Math3D.Vec4(-1*scale, -1*scale,    1*scale,   1)]

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

    for gObj in scene.gameObjects:
        gObj.myMesh.ProjectedPoints.clear()
        scene.Refresh = False
        for point in gObj.myMesh.points:
            newPoint = point*gObj.transform.Matrix
            newPoint = newPoint*scene.Camera.createLookat().inverse()
            newPoint = newPoint*scene.Camera.createProjMat()
            if newPoint[3] != 1:
                newPoint[0] = newPoint[0]/newPoint[3]
                newPoint[1] = newPoint[1]/newPoint[3]
                newPoint[2] = newPoint[2]/newPoint[3]

            gObj.myMesh.ProjectedPoints.append(newPoint)
    return True
