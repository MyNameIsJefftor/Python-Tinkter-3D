from __future__ import annotations
import math as math

class vec3():
    def __init__(self, x :float = 0, y :float = 0, z :float = 0) -> None:
        self.array = [x,y,z]

    def x(self)->float:
        return self.array[0]

    def y(self)->float:
        return self.array[1]

    def z(self)->float:
        return self.array[2]

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __eq__(self, other):
        if not isinstance(other, vec3):
            return False
        for i in range(len(self.array)):
            if self.array[i] != other.array[i]:
                return False
        return True

class vec4():
    def __init__(self, x :float = 0.0, y :float = 0, z :float = 0, w :float= 0) -> None:
        self.array = [x,y,z,w]

    def x(self)->float:
        return self.array[0]

    def y(self)->float:
        return self.array[1]

    def z(self)->float:
        return self.array[2]

    def w(self)->float:
        return self.array[3]

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __eq__(self, other):
        if not isinstance(other, vec4):
            return False
        for i in range(4):
            if other.array[i] != self.array[i]:
                return False
        return True

    def __mul__(self, other: Mat3x3)->vec4:
        if isinstance(other, Mat3x3):
            mat3 = Mat3x3(other)
            storage = vec4()
            storage.array[0] = self.array[0]*mat3.matrix[0][0]+self.array[1]*mat3.matrix[0][1]+self.array[2]*mat3.matrix[0][2]
            storage.array[1] = self.array[0]*mat3.matrix[1][0]+self.array[1]*mat3.matrix[1][1]+self.array[2]*mat3.matrix[1][2]
            storage.array[2] = self.array[0]*mat3.matrix[2][0]+self.array[1]*mat3.matrix[2][1]+self.array[2]*mat3.matrix[2][2]
            storage.array[3] = self.array[3]
            return storage

        if isinstance(other, Mat4x4):
            mat3 = Mat4x4(other)
            storage = vec4()
            storage.array[0] = self.array[0]*mat3.matrix[0][0]+self.array[1]*mat3.matrix[0][1]+self.array[2]*mat3.matrix[0][2]+self.array[3]*mat3.matrix[0][3]
            storage.array[1] = self.array[0]*mat3.matrix[1][0]+self.array[1]*mat3.matrix[1][1]+self.array[2]*mat3.matrix[1][2]+self.array[3]*mat3.matrix[1][3]
            storage.array[2] = self.array[0]*mat3.matrix[2][0]+self.array[1]*mat3.matrix[2][1]+self.array[2]*mat3.matrix[2][2]+self.array[3]*mat3.matrix[2][3]
            storage.array[3] = self.array[0]*mat3.matrix[3][0]+self.array[1]*mat3.matrix[3][1]+self.array[2]*mat3.matrix[3][2]+self.array[3]*mat3.matrix[3][3]
            return storage

        return None



# row x column
class Mat3x3():
    def __init__(self, array = [vec3(1,0,0),vec3(0,1,0),vec3(0,0,1)]) -> None:
        self.matrix = array

    def __getitem__(self, key):
        return self.matrix[key]

    def __mul__(self,other : Mat3x3) -> Mat3x3:

        if not isinstance(other, Mat3x3):
            return None
        output = Mat3x3(array=[vec3(),vec3(),vec3()])

        # top row
        output.matrix[0][0] = self.matrix[0][0]*other.matrix[0][0]+self.matrix[0][1]*other.matrix[1][0]+self.matrix[0][2]*other.matrix[2][0]
        output.matrix[0][1] = self.matrix[0][0]*other.matrix[0][1]+self.matrix[0][1]*other.matrix[1][1]+self.matrix[0][2]*other.matrix[2][1]
        output.matrix[0][2] = self.matrix[0][0]*other.matrix[0][2]+self.matrix[0][1]*other.matrix[1][2]+self.matrix[0][2]*other.matrix[2][2]

        # middle row
        output.matrix[1][0] = self.matrix[1][0]*other.matrix[0][0]+self.matrix[1][1]*other.matrix[1][0]+self.matrix[1][2]*other.matrix[2][0]
        output.matrix[1][1] = self.matrix[1][0]*other.matrix[0][1]+self.matrix[1][1]*other.matrix[1][1]+self.matrix[1][2]*other.matrix[2][1]
        output.matrix[1][2] = self.matrix[1][0]*other.matrix[0][2]+self.matrix[1][1]*other.matrix[1][2]+self.matrix[1][2]*other.matrix[2][2]

        # bottom row
        output.matrix[2][0] = self.matrix[2][0]*other.matrix[0][0]+self.matrix[2][1]*other.matrix[1][0]+self.matrix[2][2]*other.matrix[2][0]
        output.matrix[2][1] = self.matrix[2][0]*other.matrix[0][1]+self.matrix[2][1]*other.matrix[1][1]+self.matrix[2][2]*other.matrix[2][1]
        output.matrix[2][2] = self.matrix[2][0]*other.matrix[0][2]+self.matrix[2][1]*other.matrix[1][2]+self.matrix[2][2]*other.matrix[2][2]

        return output

    def __eq__(self, other : Mat3x3) -> bool:
        if not isinstance(other, Mat3x3):
            return False
        for i in range(len(self.matrix)):
            if not self.matrix[i] == other.matrix[i]:
                return False
        return True

    __slots__ = ['matrix']

class Mat4x4():
    def __init__(self, array = [vec4(1,0,0,0),vec4(0,1,0,0),vec4(0,0,1,0),vec4(0,0,0,1)]) -> None:
        self.matrix = array

    def __eq__(self, other :Mat4x4) -> bool:
        if not isinstance(other, Mat4x4):
            return False
        for i in range(len(self.matrix)):
            if not self.matrix[i] == other.matrix[i]:
                return False
        return True

    def __mul__(self,other : Mat4x4) -> Mat4x4:
        output = Mat4x4(array=[vec4(),vec4(),vec4(),vec4()])

        # row 0
        output.matrix[0][0] = self.matrix[0][0]*other.matrix[0][0]+self.matrix[0][1]*other.matrix[1][0]+self.matrix[0][2]*other.matrix[2][0]+self.matrix[0][3]*other.matrix[3][0]
        output.matrix[0][1] = self.matrix[0][0]*other.matrix[0][1]+self.matrix[0][1]*other.matrix[1][1]+self.matrix[0][2]*other.matrix[2][1]+self.matrix[0][3]*other.matrix[3][1]
        output.matrix[0][2] = self.matrix[0][0]*other.matrix[0][2]+self.matrix[0][1]*other.matrix[1][2]+self.matrix[0][2]*other.matrix[2][2]+self.matrix[0][3]*other.matrix[3][2]
        output.matrix[0][3] = self.matrix[0][0]*other.matrix[0][3]+self.matrix[0][1]*other.matrix[1][3]+self.matrix[0][2]*other.matrix[2][3]+self.matrix[0][3]*other.matrix[3][3]

        # row 1
        output.matrix[1][0] = self.matrix[1][0]*other.matrix[0][0]+self.matrix[1][1]*other.matrix[1][0]+self.matrix[1][2]*other.matrix[2][0]+self.matrix[1][3]*other.matrix[3][0]
        output.matrix[1][1] = self.matrix[1][0]*other.matrix[0][1]+self.matrix[1][1]*other.matrix[1][1]+self.matrix[1][2]*other.matrix[2][1]+self.matrix[1][3]*other.matrix[3][1]
        output.matrix[1][2] = self.matrix[1][0]*other.matrix[0][2]+self.matrix[1][1]*other.matrix[1][2]+self.matrix[1][2]*other.matrix[2][2]+self.matrix[1][3]*other.matrix[3][2]
        output.matrix[1][3] = self.matrix[1][0]*other.matrix[0][3]+self.matrix[1][1]*other.matrix[1][3]+self.matrix[1][2]*other.matrix[2][3]+self.matrix[1][3]*other.matrix[3][3]

        # row 2
        output.matrix[2][0] = self.matrix[2][0]*other.matrix[0][0]+self.matrix[2][1]*other.matrix[1][0]+self.matrix[2][2]*other.matrix[2][0]+self.matrix[2][3]*other.matrix[3][0]
        output.matrix[2][1] = self.matrix[2][0]*other.matrix[0][1]+self.matrix[2][1]*other.matrix[1][1]+self.matrix[2][2]*other.matrix[2][1]+self.matrix[2][3]*other.matrix[3][1]
        output.matrix[2][2] = self.matrix[2][0]*other.matrix[0][2]+self.matrix[2][1]*other.matrix[1][2]+self.matrix[2][2]*other.matrix[2][2]+self.matrix[2][3]*other.matrix[3][2]
        output.matrix[2][3] = self.matrix[2][0]*other.matrix[0][3]+self.matrix[2][1]*other.matrix[1][3]+self.matrix[2][2]*other.matrix[2][3]+self.matrix[2][3]*other.matrix[3][3]

        # row 3
        output.matrix[3][0] = self.matrix[3][0]*other.matrix[0][0]+self.matrix[3][1]*other.matrix[1][0]+self.matrix[3][2]*other.matrix[2][0]+self.matrix[3][3]*other.matrix[3][0]
        output.matrix[3][1] = self.matrix[3][0]*other.matrix[0][1]+self.matrix[3][1]*other.matrix[1][1]+self.matrix[3][2]*other.matrix[2][1]+self.matrix[3][3]*other.matrix[3][1]
        output.matrix[3][2] = self.matrix[3][0]*other.matrix[0][2]+self.matrix[3][1]*other.matrix[1][2]+self.matrix[3][2]*other.matrix[2][2]+self.matrix[3][3]*other.matrix[3][2]
        output.matrix[3][3] = self.matrix[3][0]*other.matrix[0][3]+self.matrix[3][1]*other.matrix[1][3]+self.matrix[3][2]*other.matrix[2][3]+self.matrix[3][3]*other.matrix[3][3]

        return output

    __slots__ = ["matrix"]

