from matrix import *

m = Matrix([[1, 6, 3], [-2, 6, 1], [8, 4, -9]])

print("\nThe starting matrix is:\n" + str(m))

print("\nThe determinant of this matrix is: " + str(m.determinant()))

print("\nThe trace of this matrix is: " + str(m.trace()))

print("\nThe transpose of this matrix is:\n" + str(m.transpose()))

print("\nThe matrix added to 1 from the right is:\n" + str(m + 1))

print("\nThe matrix added to 1 from the left is:\n" + str(1 + m))

print("\nThe matrix minus 1 is:\n" + str(m - 1))

print("\nOne minus the matrix is:\n" + str(1 - m))

print("\nThe matrix multipled by 2 from the right is:\n" + str(m * 2))

print("\nThe matrix multipled by 2 from the left is:\n" + str(2 * m))

print("\nThe matrix multipled by itself is:\n" + str(m * m))

print("\nThe matrix minus itself squared is:\n" + str(m - m * m))

print("\nThe inverse of the matrix is:\n" + str(m.inverse()))

print()

# Correct output:

"""

The starting matrix is:
+1.00E+00 +6.00E+00 +3.00E+00
-2.00E+00 +6.00E+00 +1.00E+00
+8.00E+00 +4.00E+00 -9.00E+00

The determinant of this matrix is: -286.0

The trace of this matrix is: -2.0

The transpose of this matrix is:
+1.00E+00 -2.00E+00 +8.00E+00
+6.00E+00 +6.00E+00 +4.00E+00
+3.00E+00 +1.00E+00 -9.00E+00

The matrix added to 1 from the right is:
+2.00E+00 +6.00E+00 +3.00E+00
-2.00E+00 +7.00E+00 +1.00E+00
+8.00E+00 +4.00E+00 -8.00E+00

The matrix added to 1 from the left is:
+2.00E+00 +6.00E+00 +3.00E+00
-2.00E+00 +7.00E+00 +1.00E+00
+8.00E+00 +4.00E+00 -8.00E+00

The matrix minus 1 is:
+0.00E+00 +6.00E+00 +3.00E+00
-2.00E+00 +5.00E+00 +1.00E+00
+8.00E+00 +4.00E+00 -1.00E+01

One minus the matrix is:
+0.00E+00 -6.00E+00 -3.00E+00
+2.00E+00 -5.00E+00 -1.00E+00
-8.00E+00 -4.00E+00 +1.00E+01

The matrix multipled by 2 from the right is:
+2.00E+00 +1.20E+01 +6.00E+00
-4.00E+00 +1.20E+01 +2.00E+00
+1.60E+01 +8.00E+00 -1.80E+01

The matrix multipled by 2 from the left is:
+2.00E+00 +1.20E+01 +6.00E+00
-4.00E+00 +1.20E+01 +2.00E+00
+1.60E+01 +8.00E+00 -1.80E+01

The matrix multipled by itself is:
+1.30E+01 +5.40E+01 -1.80E+01
-6.00E+00 +2.80E+01 -9.00E+00
-7.20E+01 +3.60E+01 +1.09E+02

The matrix minus itself squared is:
-1.20E+01 -4.80E+01 +2.10E+01
+4.00E+00 -2.20E+01 +1.00E+01
+8.00E+01 -3.20E+01 -1.18E+02

The inverse of the matrix is:
+2.03E-01 -2.31E-01 +4.20E-02
+3.50E-02 +1.15E-01 +2.45E-02
+1.96E-01 -1.54E-01 -6.29E-02

"""
