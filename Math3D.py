from __future__ import annotations
from math import cos, sin, tan, radians

class Vec3():
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.array = [x, y, z]

    def x(self) -> float:
        return self.array[0]

    def y(self) -> float:
        return self.array[1]

    def z(self) -> float:
        return self.array[2]

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __eq__(self, other):
        if not isinstance(other, Vec3):
            return False
        for i in range(len(self.array)):
            if self.array[i] != other.array[i]:
                return False
        return True


class Vec4():
    def __init__(self,
                 x: float = 0.0, y: float = 0, z: float = 0,
                 w: float = 0) -> None:
        self.array = [x, y, z, w]

    def x(self) -> float:
        return self.array[0]

    def y(self) -> float:
        return self.array[1]

    def z(self) -> float:
        return self.array[2]

    def w(self) -> float:
        return self.array[3]

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __eq__(self, other):
        if not isinstance(other, Vec4):
            return False
        for i in range(4):
            if other.array[i] != self.array[i]:
                return False
        return True

    def __mul__(self, other: Mat3x3) -> Vec4:
        if isinstance(other, Mat3x3):
            storage = Vec4()
            for y in range(0, 3):
                for x in range(0, 3):
                    storage[y] = storage[y] + self[y] * other[x][y]
            storage[3] = self.w()
            return storage

        if isinstance(other, Mat4x4):
            storage = Vec4()
            for y in range(0, 4):
                for x in range(0, 4):
                    storage[y] = storage[y] + self[y] * other[x][y]
            return storage

        return None


# each vector is a row
class Mat3x3():
    def __init__(self, array=[Vec3(1, 0, 0),
                              Vec3(0, 1, 0),
                              Vec3(0, 0, 1)]) -> None:
        self.matrix = array

    def __getitem__(self, key):
        return self.matrix[key]

    def __mul__(self, other: Mat3x3) -> Mat3x3:

        if not isinstance(other, Mat3x3):
            return None

        output = Mat3x3(array=[Vec3(), Vec3(), Vec3()])
        for a in range(0, 3):
            for b in range(0, 3):
                for c in range(0, 3):
                    output[a][b] = output[a][b] + self[a][c] * other[c][b]

        return output

    def __eq__(self, other: Mat3x3) -> bool:
        if not isinstance(other, Mat3x3):
            return False
        for i in range(len(self.matrix)):
            if not self.matrix[i] == other.matrix[i]:
                return False
        return True

    __slots__ = ['matrix']


class Mat4x4():
    def __init__(self, array=[Vec4(1, 0, 0, 0),
                              Vec4(0, 1, 0, 0),
                              Vec4(0, 0, 1, 0),
                              Vec4(0, 0, 0, 1)]) -> None:
        self.matrix = array

    def __getitem__(self, key):
        return self.matrix[key]

    def __eq__(self, other: Mat4x4) -> bool:
        if not isinstance(other, Mat4x4):
            return False
        for i in range(len(self.matrix)):
            if not self.matrix[i] == other.matrix[i]:
                return False
        return True

    def __mul__(self, other: Mat4x4) -> Mat4x4:
        if not isinstance(other, Mat4x4):
            return False
        output = Mat4x4(array=[Vec4(),
                               Vec4(),
                               Vec4(),
                               Vec4()])
        for a in range(0, 4):
            for b in range(0, 4):
                for c in range(0, 4):
                    output[a][b] = output[a][b] + self[a][c] * other[c][b]
        return output

    __slots__ = ["matrix"]


def RotateX(Mat: Mat4x4, angle: float) -> None:
    angle = radians(angle)
    rotationMatrix = Mat4x4()
    rotationMatrix[1] = Vec4(0, cos(angle), -sin(angle), 0)
    rotationMatrix[2] = Vec4(0, sin(angle), cos(angle), 1)
    Mat*=rotationMatrix