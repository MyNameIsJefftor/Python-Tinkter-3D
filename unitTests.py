from __future__ import annotations
import Math3D as voidMath
import unittest


class testMat(unittest.TestCase):
    def test_vec3timesMat3x3(self):
        basemat = voidMath.Mat3x3()
        vec = voidMath.Vec4(5, 6, 4, 8)
        vec = vec*basemat
        self.assertEqual(vec, voidMath.Vec4(5, 6, 4, 8))

    def test_mat3x3SelfMul(self):
        mat1 = voidMath.Mat3x3()
        mat2 = voidMath.Mat3x3(array=[voidMath.Vec3(1, 1, 1),
                                      voidMath.Vec3(2, 2, 2),
                                      voidMath.Vec3(3, 3, 3)])
        target = mat2

        output = mat1 * mat2

        self.assertEqual(output, target)

    def test_mat4x4SelfMul(self):
        mat1 = voidMath.Mat4x4()
        mat2 = voidMath.Mat4x4(array=[voidMath.Vec4(1, 1, 1, 1),
                                      voidMath.Vec4(2, 2, 2, 2),
                                      voidMath.Vec4(3, 3, 3, 3),
                                      voidMath.Vec4(4, 4, 4, 4)])
        target = mat2
        mat1 *= mat2
        output = mat1
        self.assertEqual(output, target)

    def test_XRotation(self):
        mat = voidMath.Mat4x4()
        rotmat = voidMath.Mat4x4(array=[voidMath.Vec4(1, 0, 0, 0),
                                        voidMath.Vec4(0, 0, -1, 0),
                                        voidMath.Vec4(0, 1, 0, 0),
                                        voidMath.Vec4(0, 0, 0, 1)])

        voidMath.RotateX(mat, 90)
        self.assertEqual(mat, rotmat)

    def test_YRotation(self):
        mat = voidMath.Mat4x4()
        rotmat = voidMath.Mat4x4(array=[voidMath.Vec4(0, 0, 1, 0),
                                        voidMath.Vec4(0, 1, 0, 0),
                                        voidMath.Vec4(-1, 0, 0, 0),
                                        voidMath.Vec4(0, 0, 0, 1)])

        voidMath.RotateY(mat, 90)
        self.assertEqual(mat, rotmat)

    def test_ZRotation(self):
        mat = voidMath.Mat4x4()
        rotmat = voidMath.Mat4x4(array=[voidMath.Vec4(0, -1, 0, 0),
                                        voidMath.Vec4(1, 0, 0, 0),
                                        voidMath.Vec4(0, 0, 1, 0),
                                        voidMath.Vec4(0, 0, 0, 1)])

        voidMath.RotateZ(mat, 90)
        self.assertEqual(mat, rotmat)

    def test_2x2Determinant(self):
        det = voidMath.determinant2x2(2, 3, 1, -2)
        self.assertEqual(det, -7)

    def test_3x3Determinant(self):
        mat = voidMath.Mat3x3(array=[voidMath.Vec3(5, 0, 3),
                                     voidMath.Vec3(2, 3, 5),
                                     voidMath.Vec3(1, -2, 3)])
        det = mat.determinate()
        self.assertEqual(det, 74)

    def test_CreateSub3x3From4x4(self):
        mat4 = voidMath.Mat4x4()
        matConv = mat4.createSub3x3()
        mat3 = voidMath.Mat3x3()
        self.assertEqual(mat3, matConv)

    def test_4x4Determinant(self):
        mat = voidMath.Mat4x4(array=[voidMath.Vec4(1, 0, 4, -6),
                                     voidMath.Vec4(2, 5, 0, 3),
                                     voidMath.Vec4(-1, 2, 3, 5),
                                     voidMath.Vec4(2, 1, -2, 3)])
        det = mat.determinate()
        self.assertEqual(det, 318)


class testVec(unittest.TestCase):
    def test_Convert4to3(self):
        vec4 = voidMath.Vec4(w=1).convertToVec3()
        vec3 = voidMath.Vec3()
        self.assertEqual(vec4, vec3)


if __name__ == "__main__":
    unittest.main()
