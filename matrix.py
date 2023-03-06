class Matrix:
    # "Generate and manipulate matrix objects"

    def __init__(self, matrix):  # Object constructor
        self.rows = len(matrix)
        if not self.rows:
            raise ValueError("Invalid Matrix")
        self.cols = len(matrix[0])
        if not self.cols:
            raise ValueError("Invalid Matrix")
        self.matrix = tuple(tuple(map(float, row))
                            for row in matrix if (len(row) == self.cols))
        if not (len(self.matrix) == self.rows):
            raise ValueError("Invalid Matrix")
        self.square = (self.cols == self.rows)

    @staticmethod
    def unit(size, val=1.0):
        return Matrix(tuple(tuple(
            (float(val) if (i == j) else 0.0)
            for j in range(size))
                            for i in range(size)))

    @staticmethod
    def sign(row, col):
        return -1.0 if (int(row + col) % 2) else +1.0

    def submatrix(self, row, col):
        return Matrix(tuple(tuple(self.matrix[i][j]
                                  for j in range(self.cols) if (j != col))
                            for i in range(self.rows) if (i != row)))

    def determinant(self):
        if not self.square:
            raise ValueError("Non-Square Matrix")
        if self.rows == 1:
            return self.matrix[0][0]
        return sum((Matrix.sign(i, 0) *
                    self.matrix[i][0] *
                    self.submatrix(i, 0).determinant())
                   for i in range(self.rows))

    def trace(self):
        if not self.square:
            raise ValueError("Non-Square Matrix")
        return sum(self.matrix[i][i] for i in range(self.rows))

    def transpose(self):
        if not self.square:
            raise ValueError("Non-Square Matrix")
        if self.rows == 1:
            return self.matrix[1][0]
        return Matrix(tuple(tuple(self.matrix[j][i]
                                  for j in range(self.rows))
                            for i in range(self.cols)))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return self + Matrix.unit(self.cols, other)
        if (other.rows != self.rows) or (other.cols != self.cols):
            raise ValueError("Invalid Matrix Sum")
        return Matrix(tuple(tuple(
            (self.matrix[i][j] + other.matrix[i][j])
            for j in range(other.cols))
                            for i in range(self.rows)))

    __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            return self - Matrix.unit(self.cols, other)
        if (other.rows != self.rows) or (other.cols != self.cols):
            raise ValueError("Invalid Matrix Subtraction")
        return Matrix(tuple(tuple(
            (self.matrix[i][j] - other.matrix[i][j])
            for j in range(other.cols))
                            for i in range(self.rows)))

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Invalid Matrix Multiplication")
            result = [[0.0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            return Matrix([[other * val for val in row] for row in self.matrix])
        else:
            return NotImplemented

    __rmul__ = __mul__

    def __getitem__(self, key):
        return self.matrix[key]

    def __str__(self):
        return "\n".join(" ".join(format(val, "+9.2E")
                                  for val in row)
                         for row in self.matrix)
