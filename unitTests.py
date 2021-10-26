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


if __name__ == "__main__":
    unittest.main()
