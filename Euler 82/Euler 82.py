__author__ = 'eddolan'


def read_file():
    matrix = []
    temp = open("matrix.txt" , "r").read().split("\n")
    matrix.append([])
    for line in temp:
        temp2 = []
        temp1 = line.split(",")
        for num in temp1:
            temp2.append(int(num))
        matrix.append(temp2)
    matrix.append([])
    for x in range(0,80):
        matrix[0].append(999999)
        matrix[-1].append(999999)
    return matrix

def print_matrix(matrix):
    for row in matrix[1:81]:
        for number in row:
            print repr(number).rjust(5),
        print ""



def main():
    matrix = read_file()
    matrix1 = []
    for line in matrix:
            matrix1.append(line[:])

    # start the problem
    for x in range(78,-1,-1):
        for count in range(1,81):
            matrix1[count][x] = matrix1[count][x+1] + matrix1[count][x]
            matrix1[count][x] = min(matrix1[count][x], matrix1[count-1][x] + matrix[count][x])
        for count in range(80,0,-1):
            matrix1[count][x] = min(matrix1[count][x], matrix1[count+1][x] + matrix[count][x])

    temp = []
    for row in matrix1[1:81]:
        temp.append(row[0])
    print_matrix(matrix)
    print "\n\n\n\n\n"
    print_matrix(matrix1)

    print min(temp)






main()