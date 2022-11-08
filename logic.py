import numpy as np

class Matrix:
    rows = 0
    columns = 0
    matrix = None
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = np.zeros((rows, columns))
    
    def display(self):
        print(self.matrix)
    
    def input(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = int(input("Enter single elements by row: "))
    
    def randomize(self):
        range1 = int(input("Enter lower range of values: "))
        range2 = int(input("Enter upper range of values: "))
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = np.random.randint(range1, range2)
                
    def swapRows(self, row1, row2):
        temp = self.matrix[row1]
        self.matrix[row1] = self.matrix[row2]
        self.matrix[row2] = temp
    
    def gausJordanElimination(self):
        for i in range(self.rows):
            if self.matrix[i][i] == 0:
                self.swapRows(i, i+1)
            self.matrix[i] = self.matrix[i] / self.matrix[i][i]
            for j in range(self.rows):
                if i != j:
                    self.matrix[j] = self.matrix[j] - self.matrix[j][i] * self.matrix[i]

def main():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    
    m = Matrix(rows, columns)
    m.display()
    
    m.randomize()
    m.display()
    
    m.gausJordanElimination()
    m.display()
    
    
if __name__ == "__main__":
    main()
    
    
