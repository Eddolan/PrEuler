__author__ = 'eddolan'



def read_file():
    matrix = []
    temp = open("matrix.txt" , "r").read().split("\n")
    matrix.append([])
    for line in temp:
        temp2 = [999999]
        temp1 = line.split(",")
        for num in temp1:
            temp2.append(int(num))
        temp2.append(999999)
        matrix.append(temp2)
    matrix.append([])
    for x in range(0,80):
        matrix[0].append(999999)
        matrix[-1].append(999999)
    return matrix



def print_matrix(matrix):
    for row in matrix[1:81]:
        for number in row[1:81]:
            print repr(number).rjust(6),
        print ""


def main():
    matrix = read_file()
    matrix1 = []
    print_matrix(matrix)
    for line in matrix:
        matrix1.append(line[:])

    print '\n\n\n'
    for count in range(159,0,-1):
        for i in range(1,count):
            j = count-i
            if j<=80 and i <=80:
                matrix[i][j]= min(matrix[i][j] + matrix[i+1][j], matrix[i][j] + matrix[i][j+1])

    for q in range(200):
        for count in range(159,0,-1):
            for i in range(1,count):
                j = count-i
                if j<80 and i <80:
                   matrix[i][j]= min(matrix[i][j] , matrix1[i][j] + matrix[i][j-1] , matrix1[i][j] + matrix[i-1][j], matrix1[i][j] + matrix[i][j+1],  matrix1[i][j] + matrix[i+1][j])

    print_matrix(matrix)

    min_vector = []
    for x in range(1,81):
        min_vector.append(matrix[x][1])
    print  min_vector



main()
