from __future__ import annotations
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
    def __init__(self, position=Math3D.Vec4(), target=Math3D.Vec4(z=1),
                 nearPlane=1, farPlane=10) -> None:
        self.transform = None
        self.near = nearPlane
        self.far = farPlane
        self.target = Math3D.Vec4
        self.position = position
        self.forward = Math3D.normalize(position - target)
        self.up = Math3D.Vec4(0, 1, 0, 0)
        self.right = Math3D.normalize(Math3D.cross(self.up, self.forward))
        self.view = self.createLookat()

    def createLookat(self) -> Math3D.Mat4x4:
        mat1 = Math3D.Mat4x4()
        mat1[0] = Math3D.Vec4(self.right[0], self.right[1], self.right[2], 0)
        mat1[1] = Math3D.Vec4(self.up[0], self.up[1], self.up[2], 0)
        mat1[2] = Math3D.Vec4(self.forward[0], self.forward[1],
                              self.forward[2])

        mat2 = Math3D.Mat4x4()
        mat2[0][3] = -self.position.x()
        mat2[1][3] = -self.position.y()
        mat2[2][3] = -self.position.z()

        return mat1*mat2


class gameObject:
    def __init__(self) -> None:
        self.myMesh = Mesh()
        self.transform = Math3D.Mat4x4()


class Scene:
    def __init__(self) -> None:
        self.gameObjects = [gameObject()]
        self.Camera = Camera()

    def addObject(self, obj: gameObject):
        if not isinstance(obj, gameObject):
            return
        self.gameObjects.append(obj)


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


def Draw(scene: Scene):
    if(len(scene.gameObjects) <= 0):
        return

    projMat = Math3D.lookAt()
    for gObj in scene.gameObjects:
        gObj.myMesh.ProjectedPoints.clear()
        for point in gObj.myMesh.points:
            gObj.myMesh.ProjectedPoints.append(point*gObj.transform*scene.Camera.view*projMat)
