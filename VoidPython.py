import Math3D


class Mesh():
    def __init__(self):
        self.points = [Math3D.Vec4()]
        self.pairs = [Math3D.Vec3()]


class Transform():
    def __init__(self):
        self.position = Math3D.Mat4x4()
        self.rotation = Math3D.Mat4x4()
        self.scale = Math3D.Vec3()


class Camera:
    def __init__(self, position, nearPlane=1, farPlane=10) -> None:
        self.transform = None
        self.near = nearPlane
        self.far = farPlane

    __slots__ = ['width', 'height', 'distance']


class Object:
    def __init__(self) -> None:
        self.mesh = None
        self.transform = None

    __slots__ = ["Mesh", "Position"]
