from __future__ import annotations
from math import cos, sin, radians, sqrt


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

    def __sub__(Self, other) -> Vec3:
        output = Vec3()
        for x in range(0, 3):
            output[x] = Self[x] - other[x]

        return output


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
            a = round(self.array[i], 4)
            b = round(other.array[i], 4)
            if a != b:
                return False
        return True

    def __add__(self, other: Vec4) -> Vec4:
        if not isinstance(other, Vec4):
            return

        output = Vec4()
        output[0] = self.x() + other.x()
        output[1] = self.y() + other.y()
        output[2] = self.z() + other.z()
        output[3] = self.w() + other.w()
        return output

    def __sub__(self, other) -> Vec4:
        output = Vec4()
        output[0] = self.x() - other.x()
        output[1] = self.y() - other.y()
        output[2] = self.z() - other.z()
        output[3] = self.w() - other.w()
        return output

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

        if isinstance(other, Vec4):
            storage = Vec4()
            for i in range(0, 4):
                storage[i] = self[i] * other[i]
            return storage

        return None

    # Vector Math
    def normalize(self) -> Vec4:
        mag = sqrt((self.x() * self.x()) + (self.y() * self.y()) + (self.z() * self.z()))
        output = Vec4()
        output[0] = self[0] / mag
        output[1] = self[1] / mag
        output[2] = self[2] / mag
        return output

    def convertToVec3(self, Cut: int = 3) -> Vec3:
        if Cut > 3 or Cut < 0:
            raise Exception("Tried Cutting outside the bounds convertToVec3")

        output = []
        for x in range(4):
            if x == Cut:
                continue
            output.append(self.array[x].__float__())
        output = Vec3(output[0], output[1], output[2])
        return output


# each vector is a row
class Mat3x3():
    def __init__(self, array=[Vec3(1, 0, 0),
                              Vec3(0, 1, 0),
                              Vec3(0, 0, 1)]) -> None:
        self.matrix = array

    def __getitem__(self, key):
        return self.matrix[key]

    def __rmul__(self, other: Mat3x3) -> Mat3x3:

        if not isinstance(other, Mat3x3):
            return None

        output = Mat3x3(array=[Vec3(), Vec3(), Vec3()])
        for a in range(0, 3):
            for b in range(0, 3):
                for c in range(0, 3):
                    output[a][b] = output[a][b] + self[a][c] * other[c][b]

        return output

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

    def determinate(self) -> float:
        mat = self.matrix
        output = mat[0][0] * determinant2x2(mat[1][1], mat[1][2], mat[2][1], mat[2][2])
        output = output - mat[0][1] * determinant2x2(mat[1][0], mat[1][2], mat[2][0], mat[2][2])
        output = output + mat[0][2] * determinant2x2(mat[1][0], mat[1][1], mat[2][0], mat[2][1])

        return output

    __slots__ = ['matrix']


class Mat4x4():
    def __init__(self, array=[Vec4(1, 0, 0, 0),
                              Vec4(0, 1, 0, 0),
                              Vec4(0, 0, 1, 0),
                              Vec4(0, 0, 0, 1)]) -> None:
        self.matrix = array

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, other):
        self.matrix[key] = other

    def __eq__(self, other: Mat4x4) -> bool:
        if not isinstance(other, Mat4x4):
            return False
        for i in range(len(self.matrix)):
            if not self.matrix[i] == other.matrix[i]:
                return False
        return True

    def __mul__(self, other: Mat4x4) -> Mat4x4:
        if isinstance(other, Mat4x4):
            output = Mat4x4(array=[Vec4(),
                                   Vec4(),
                                   Vec4(),
                                   Vec4()])
            for a in range(0, 4):
                for b in range(0, 4):
                    for c in range(0, 4):
                        output[a][b] = output[a][b] + self[a][c] * other[c][b]
            return output
        elif isinstance(other, Vec4):
            storage = Vec4()
            for y in range(0, 4):
                for x in range(0, 4):
                    storage[y] = storage[y] + other[y] * self[x][y]
            return storage

        return None

    # Cut a row and column off to create a 3x3 matrix
    def createSub3x3(self, cutRow: int = 3, cutCol: int = 3) -> Mat3x3:

        output = []
        for row in range(4):
            if row == cutRow:
                continue

            output.append(self.matrix[row].convertToVec3(cutCol))

        output = Mat3x3(array=[output[0], output[1], output[2]])

        return output

    def determinate(self) -> float:
        arr = [Mat3x3()]
        arr.clear()
        for x in range(4):
            arr.append(self.createSub3x3(0, x))

        output = self.matrix[0][0] * arr[0].determinate()
        output = output - self.matrix[0][1] * arr[1].determinate()
        output = output + self.matrix[0][2] * arr[2].determinate()
        output = output - self.matrix[0][3] * arr[3].determinate()

        return output

    # Row become Columns
    def transpose(self) -> Mat4x4:
        mat = self.matrix
        return Mat4x4(array=[Vec4(mat[0][0], mat[1][0], mat[2][0], mat[3][0]),
                             Vec4(mat[0][1], mat[1][1], mat[2][1], mat[3][1]),
                             Vec4(mat[0][2], mat[1][2], mat[2][2], mat[3][2]),
                             Vec4(mat[0][3], mat[1][3], mat[2][3], mat[3][3])])

    def inverse(self) -> Mat4x4:
        output = Mat4x4()
        for row in range(4):
            for col in range(4):
                output[row][col] = self.createSub3x3(row, col).determinate()*0.5

        output = output.transpose()
        return output

    # Right Handed Rotations
    def RotateX(self, angle: float) -> None:
        angle = radians(angle)
        rotationMatrix = Mat4x4()
        rotationMatrix[1] = Vec4(0, cos(angle), -sin(angle), 0)
        rotationMatrix[2] = Vec4(0, sin(angle), cos(angle), 0)
        self.matrix *= rotationMatrix

    def RotateY(self, angle: float) -> None:
        angle = radians(angle)
        rotationMatrix = Mat4x4()
        rotationMatrix[0] = Vec4(cos(angle), 0, sin(angle), 0)
        rotationMatrix[2] = Vec4(-sin(angle), 0, cos(angle), 0)
        self.matrix *= rotationMatrix

    def RotateZ(self, angle: float) -> None:
        angle = radians(angle)
        rotationMatrix = Mat4x4()
        rotationMatrix[0] = Vec4(cos(angle), -sin(angle), 0, 0)
        rotationMatrix[1] = Vec4(sin(angle), cos(angle), 0, 0)
        self.matrix *= rotationMatrix

    __slots__ = ["matrix"]


def cross(vec1: Vec4, vec2: Vec4) -> Vec4:
    output = Vec4()
    output[0] = vec1.y() * vec2.z() - vec2.y() * vec1.z()
    output[1] = vec1.x() * vec2.z() - vec2.x() * vec1.z()
    output[2] = vec1.x() * vec2.y() - vec2.x() * vec1.y()

    return output


def dot(vec1: Vec4, vec2: Vec4) -> float:
    return vec1.x()*vec2.x() + vec1.y()*vec2.y() + vec1.z()*vec2.z()


# ExtraMatrix Functions
def determinant2x2(topLeft: float = 0, topRight: float = 0,
                   botLeft: float = 0, botRight: float = 0) -> float:

    return (topLeft * botRight) - (topRight * botLeft)
