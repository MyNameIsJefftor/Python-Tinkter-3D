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
        self.position = self.position + Math3D.Vec4(x=0.1)

    def MoveNegX(self):
        self.position = self.position + Math3D.Vec4(x=-0.1)

    def MovePosY(self):
        self.position = self.position + Math3D.Vec4(y=0.1)

    def MoveNegY(self):
        self.position = self.position + Math3D.Vec4(y=-0.1)

    def MovePosZ(self):
        self.position = self.position + Math3D.Vec4(z=0.1)

    def MoveNegZ(self):
        self.position = self.position + Math3D.Vec4(z=-0.1)

    def createLookat(self,
                     target: Math3D.Vec4 = Math3D.Vec4(0, 0, 1, 0)) -> Math3D.Mat4x4:
        # Look
        zAxis = Math3D.normalize(self.position - target)

        # Right
        xAxis = Math3D.normalize(Math3D.cross(self.up, zAxis))

        # Up
        yAxis = self.up

        output = Math3D.Mat4x4(array=[
                                      Math3D.Vec4(xAxis.x(), yAxis.x(), zAxis.x(), 0),
                                      Math3D.Vec4(xAxis.y(), yAxis.y(), zAxis.y(), 0),
                                      Math3D.Vec4(xAxis.z(), yAxis.z(), zAxis.z(), 0),
                                      Math3D.Vec4(Math3D.dot(xAxis, self.position),
                                                  Math3D.dot(yAxis, self.position),
                                                  Math3D.dot(zAxis, self.position),
                                                  1)])

        return (output)

    def createProjMat(self, fov: int = 90, aspectRatio: float = 1.0) -> Math3D.Mat4x4:
        scale = fov/2
        scale = radians(scale).real
        scale = 1/tan(scale).real
        extraVal1 = (self.far/(self.far - self.near))
        extraVal2 = ((self.far*self.near)/(self.far-self.near))
        output = Math3D.Mat4x4(array=[Math3D.Vec4(scale * aspectRatio, 0, 0, 0),
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
        FinalMat = gObj.transform
        FinalMat = FinalMat*scene.Camera.createProjMat()
        FinalMat = FinalMat*scene.Camera.createLookat()
        for point in gObj.myMesh.points:
            print("--")
            print("cameraPos")
            print(scene.Camera.position.x(), " ", scene.Camera.position.y(),
                  " ", scene.Camera.position.z())
            print("Local")
            tempPoint = point
            print(tempPoint.z())
            print("World")
            tempPoint = tempPoint*gObj.transform
            print(tempPoint.z())
            print("Camera")
            tempPoint = tempPoint*scene.Camera.createLookat()
            print(tempPoint.z())
            print("Screen")
            tempPoint = tempPoint*scene.Camera.createProjMat()
            print(tempPoint.z())
            print("--")
            newPoint = point*FinalMat
            if newPoint[3] != 1:
                newPoint[0] = newPoint[0]/newPoint[3]
                newPoint[1] = newPoint[1]/newPoint[3]
                newPoint[2] = newPoint[2]/newPoint[3]
                newPoint[3] = 1

            gObj.myMesh.ProjectedPoints.append(newPoint)
    return True
