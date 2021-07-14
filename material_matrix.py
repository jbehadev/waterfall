import numpy

class material_matrix():
    material_matrix = []
    def __init__(self, length, height) -> None:
        for x in range(0,320):
            rows = []
            for y in range(0,240):
                rows.append(0)
            self.material_matrix.append(rows)

    def set_material(self, x, y, m):
        self.material_matrix[x][y] = m
    
    def print_matrix(self):
        print(self.material_matrix)

    def as_array(self):
        return numpy.asarray(self.material_matrix)