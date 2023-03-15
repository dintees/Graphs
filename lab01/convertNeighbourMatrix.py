###################convert neighbour matrix to neighbour list########################
def convertNeighbourMatrixToList(neighourhoodMatrix) : 
    rows = len(neighourhoodMatrix)
    cols = len(neighourhoodMatrix[0])
    singleNeighourhoodList = [[0 for x in range(rows)]]
    neighourhoodList = []

    for x in range (rows) :
        neighourhoodList.append([])
    
        for y in range(cols) : 
            if (neighourhoodMatrix[x][y] == 1) :
                neighourhoodList[-1].append(y + 1)
    return neighourhoodList


def showNeighbourhoodList(list) : 
    length = len(list)
    for idx in range(length) :
        print(list[idx])
    
    print()
    
###################convert neighbour matrix to matirx of incidence#####################
def convertNeighbourMatrixToMatrixOfIncidence(neighourhoodMatrix) : 
    rows = len(neighourhoodMatrix)
    cols = len(neighourhoodMatrix[0])
    howManyEgdeInGraph = 0
    listOfTuplesEdges = []
    listOfTuplesEdges.append([])
    for x in range (rows) : 
        for y in range(cols) : 
            if (y > x) :
                if (neighourhoodMatrix[x][y] == 1) :
                    egdeTuple = (x + 1,y + 1)
                    listOfTuplesEdges[-1].append(egdeTuple)
                    howManyEgdeInGraph = howManyEgdeInGraph + 1

    matrixIncident = [[0 for x in range(howManyEgdeInGraph)] for y in range(rows)]
    for y in range(howManyEgdeInGraph) : 
        firstTopNumber = listOfTuplesEdges[0][y][0]
        secondTopNumber = listOfTuplesEdges[0][y][1]
        matrixIncident[firstTopNumber - 1][y] = 1
        matrixIncident[secondTopNumber - 1][y] = 1
    
    return matrixIncident


def showMatrixOfIncidence(matrix) : 
    length = len(matrix)
    for idx in range(length) :
        print(matrix[idx])
    
    print()
    

####################################################################################
if __name__ == "__main__":
    neighourhoodMatrix = [[0,1,0,0,1], 
                      [1,0,1,1,1], 
                      [0,1,0,1,0],
                      [0,1,1,0,1],
                      [1,1,0,1,0]]

    list = convertNeighbourMatrixToList(neighourhoodMatrix)
    matrixIncidence = convertNeighbourMatrixToMatrixOfIncidence(neighourhoodMatrix)

    showNeighbourhoodList(list)
    showMatrixOfIncidence(matrixIncidence)



