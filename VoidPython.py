
from Math3D import Math3d


class Camera:
    def __init__(self, position, nearPlane = 1, farPlane = 10) -> None:
        self.matrix = Math3d.Mat3()
        self.near = nearPlane
        self.far = farPlane

    __slots__ = ['width', 'height', 'distance']

class Object:
    def __init__(self) -> None:
        self.points = list()
        self.pairs = list()

    __slots__ = ["flatPoints", "points", "pairs"]