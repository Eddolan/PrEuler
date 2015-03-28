__author__ = 'Eddie'



class Node():
    def __init__(self):
        self.next = []

    def add_node(self , next_node):
        self.next.append( next_node )

    def get_next(self):
        if len(self.next)==0:
            pass
        else:
            return_list=[]
            for node in self.next:
                return_list.append(node)
            return return_list
    
    def remove_next(self , remove_node):
	# doesnt check for instruction validity
	self.next.remove(remove_node)

def get_connections_driver( node_list ):
    summer = 0
    for node in node_list:
        add , visited = get_connections(node , [node_list[0]] )
        summer = summer + add
    return summer


def get_connections(node , visited):
    if node in visited:
        return 0 , visited
    else:
        visited.append(node)
        mabel = 1
        if node.get_next():
            for x in node.get_next():
                if node.get_next() in visited:
                    pass
                else:
                    mabel , visited = get_connections( x , visited)
                    return mabel , visited
        else:
            return 1 , visited
    

def get_input():
    text = open("Euler107.txt" , 'r').read()
    mabel =  [x.split(",") for x in text.split('\n')]
    return mabel

def find_dist( matrix , dist):
    coords = []
    #returns x,y of those distances
    for x in range(len(matrix)):
        for y in range(x,len(matrix)):
	        if matrix[x][y] == dist:
	    	    coords.append([x,y])
    return coords

def main():
    distances = []
    mabel = get_input()
    for row in range(len(mabel)):
        for column in range(len(mabel)):
            try:
                mabel[row][column] = int(mabel[row][column])
                if column>row:
                    distances.append(mabel[row][column])
            except:
                mabel[row][column] = ""
    distances.sort()
    print distances
    node_list = []
    for x in range(len(mabel)):
        node_list.append(Node())
    conns = 1
    dist = distances[0]
    print dist

    x = find_dist(mabel,distances[0])
    node_list[x[0][0]].add_node(node_list[x[0][1]])

    for length in distances[1:]:
        paths = find_dist( mabel , length)
        for path in paths:
            node_list[path[0]].add_node(node_list[path[1]])
            if get_connections_driver(node_list) > conns:
                conns = get_connections_driver(node_list)
                if conns >= len(mabel):
                    dist = dist + length

            else:
                node_list[path[0]].remove_next(node_list[path[1]])


    




print main()

