import Math3D


class Mesh():
    def __init__(self):
        self.points = [Math3D.Vec4()]
        self.sets = [Math3D.Vec3()]


class Transform():
    def __init__(self):
        self.Matrix = Math3D.Mat4x4
        self.Position = Math3D.Vec4
        self.Rotation = Math3D.Vec4


class Camera:
    def __init__(self, position, target, nearPlane=1, farPlane=10) -> None:
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
        mat2[0][3] = -self.position.x
        mat2[1][3] = -self.position.y
        mat2[2][3] = -self.position.z

        return mat1*mat2

    __slots__ = ['width', 'height', 'distance']


class Object:
    def __init__(self) -> None:
        self.mesh = None
        self.transform = None

    __slots__ = ["Mesh", "Position"]


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
