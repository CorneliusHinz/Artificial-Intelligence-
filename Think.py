from math import *
import sys
import random

class Think2:
    # Construkt the class Think2
    def __init__(self, pName, InputNodes, HiddenLayer, HiddenNodes, OutputNodes):
        self.N = []  # Contains all Nodes from the Network
        self.W = []  # Contains all Weights from the Network
        self.B = []  # Contains all Bias from the Network
        self.name = pName
        self.build_structur(InputNodes, HiddenLayer, HiddenNodes, OutputNodes)
        self.network_save()

    def build_structur(self, InputNodes, HiddenLayer, HiddenNodes, OutputNodes):
        # Create a Network witout hidden layers
        if HiddenLayer == 0:
            self.N.append(matrix_create(InputNodes, 1))
            self.W.append(matrix_create(OutputNodes, InputNodes))
            self.N.append(matrix_create(OutputNodes, 1))
            self.B.append(matrix_create(OutputNodes, 1))
        # Create a Network with hidden layer
        else:
            self.N.append(matrix_create(InputNodes, 1))
            self.W.append(matrix_create(HiddenNodes, InputNodes))
            for h in range(HiddenLayer):
                self.N.append(matrix_create(HiddenNodes, 1))
                self.B.append(matrix_create(HiddenNodes, 1))
            for n in range(HiddenLayer-1):
                self.W.append(matrix_create(HiddenNodes, HiddenNodes))
            self.W.append(matrix_create(OutputNodes, HiddenNodes))
            self.N.append(matrix_create(OutputNodes, 1))
            self.B.append(matrix_create(OutputNodes, 1))

    def matrix_activate(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                matrix[r][c] = round((2/(1+(exp(-2*(matrix[r][c]))))-1), 2)
        return matrix

    def feed_forward(self):
        for n in range(len(self.N)):
            if n != 0:
                self.N[n] = self.matrix_activate((matrix_add((matrix_multiply(self.W[n - 1], self.N[n - 1])), self.B[n - 1])))

    def weights_randomize(self):
        for w in range(len(self.W)):
            for r in range(len(self.W[w])):
                for s in range(len(self.W[w][r])):
                    self.W[w][r][s] = round(random.uniform(-1, 1), 6)

    def bias_randomize(self):
        for b in range(len(self.B)):
            for c in range(len(self.B[b])):
                for d in range(len(self.B[b][c])):
                    self.B[b][c][d] = round(random.uniform(-1, 1), 6)

    def set_input_layer(self, imatrix, update):
        input = matrix_shape(imatrix, len(imatrix), 1)
        if matrix_dimensions(input) != matrix_dimensions(self.N[0]):
            sys.exit("error in size of input array ")
        self.N[0] = imatrix
        if update == True:
            self.feed_forward()

    def set_input_node(self, node, value, update):
        self.N[0][node][0] = value
        if update == True:
            self.feed_forward()

    def print_network(self):
        print("Nodes", self.N)
        print("Weights", self.W)
        print("Bias", self.B)

    def play(self):
        for p in range(100):
            self.set_input_layer([[random.uniform(-100, 100)], [random.uniform(-100, 100)]], True)
            print(self.N[-1])

    def network_save(self):
        # save Weights
        file_write(self.name + "_Weight.txt", self.W)
        # save Bias
        file_write(self.name + "_Bias.txt", self.B)

    def network_load(self):
        # load bias
        dBias = file_read(self.name+ "_Bias.txt")
        index = 0
        for w in range(len(self.B)):
            for r in range(len(self.B[w])):
                for s in range(len(self.B[w][r])):
                    self.B[w][r][s] = dBias[index]
                    index += 1
        # load Weights
        dWeight = file_read(self.name + "_Weight.txt")
        index = 0
        for w in range(len(self.W)):
            for r in range(len(self.W[w])):
                for s in range(len(self.W[w][r])):
                    self.W[w][r][s] = dWeight[index]
                    index += 1

########################################################################################################################
#.............................................MATH.....................................................................#
########################################################################################################################
# Methode returns a matrix
def matrix_create(rows, collums):
    m = []
    for r in range(rows):
        m.append([])
        for c in range(collums):
            m[r].append(0)
    return m
# Methode to shape a array to a matrix
def matrix_shape(array, rows, collums):
    if rows*collums != len(array):
        sys.exit("Array is to large for given matrix dimensions")
    m = []
    aIndex = 0
    for r in range(rows):
        m.append([])
        for c in range(collums):
            m[r].append(array[aIndex])
            aIndex += 1
    return m
# Methode to get the dimensions of a matrix
def matrix_dimensions(matrix):
    return [len(matrix), len(matrix[0])]

# Methode to multiply to matrixes
def matrix_multiply(matrixa, matrixb):
    dimensiona = matrix_dimensions(matrixa)
    dimensionb = matrix_dimensions(matrixb)
    if dimensiona[1] != dimensionb[0]:
        sys.exit("Error in the size of a matrix")
    m = matrix_create(dimensiona[0], dimensionb[1])
    # iterate through rows of X
    for i in range(len(matrixa)):
        # iterate through columns of Y
        for j in range(len(matrixb[0])):
            # iterate through rows of Y
            for k in range(len(matrixb)):
                m[i][j] += matrixa[i][k] * matrixb[k][j]
    return m

# Method to add to matrixes
def matrix_add(matrixa, matrixb):
    dimensiona = matrix_dimensions(matrixa)
    dimensionb = matrix_dimensions(matrixb)
    if dimensiona != dimensionb:
        sys.exit("Error in the size of matrix")
    m = matrix_create(dimensiona[0], dimensiona[1])
    for r in range(len(matrixa)):
        for c in range(len(matrixa[r])):
            m[r][c] = matrixa[r][c] + matrixb[r][c]
    return m

########################################################################################################################
#.............................................SAVE.....................................................................#
########################################################################################################################
# Methods to save and load Network arrays

# Method to wride to file
def file_write(filename, array):
    with open(filename, "w") as file:
        for w in range(len(array)):
            for r in range(len(array[w])):
                for s in range(len(array[w][r])):
                    file.write(str(array[w][r][s]) + "\n")

# Method to read file
def file_read(filename):
    with open(filename, "r") as file:
        rdata = []
        for line in file:
            rdata.append(float(line))
        #data = matrix_shape(rdata, size[0], size[1])
    #return(data)
    return(rdata)