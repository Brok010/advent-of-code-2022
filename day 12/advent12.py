#first part bfs is to find best way from set start to set stop
#second part bfs is to find best way from set stop to any start

data, StartPos, StartPosPart2, StopPos = [], [], [], []

#parsing
file = open('input.txt')
x, y = 0, 0
for row in file:
    rows = []
    for each in row.strip():
        if each == 'S':
            StartPosPart1 = [x, y]
            rows.append('a')
        elif each == 'E':
            StopPosPart1 = [x, y]
            StartPosPart2 = [x, y]
            rows.append('z')
        else:
            rows.append(each)
        y += 1
    data.append(rows)
    y = 0
    x += 1

#convert letters to integers
num_data = [[(ord(letter) - 96) for letter in inner_list] for inner_list in data]

def NeighboursPart1(x, y):
    Neighbours = []
    CurentPos = num_data[x][y]
    #check all directions
    #up
    if x >= 1:
        NeighbourUp = num_data[x - 1][y]
        if NeighbourUp <= CurentPos + 1:
            Neighbours.append([x - 1, y])
    #down
    length = len(num_data)
    if x < length - 1:
        NeighbourDown = num_data[x + 1][y]
        if NeighbourDown <= CurentPos + 1:
            Neighbours.append([x + 1, y])
    
    #left
    if y >= 1:
        NeighbourLeft = num_data[x][y - 1]
        if NeighbourLeft <= CurentPos + 1:
            Neighbours.append([x, y - 1])
    #right
    row_length = len(num_data[0])
    if y < row_length - 1:
        NeighbourRight = num_data[x][y + 1]
        if NeighbourRight <= CurentPos + 1:
            Neighbours.append([x, y + 1])

    return Neighbours

def neighboursPart2(x, y):
    Neighbours = []
    CurentPos = num_data[x][y]
    #check all directions
    #up
    if x >= 1:
        NeighbourUp = num_data[x - 1][y]
        if NeighbourUp >= CurentPos - 1:
            Neighbours.append([x - 1, y])
    #down
    length = len(num_data)
    if x < length - 1:
        NeighbourDown = num_data[x + 1][y]
        if NeighbourDown >= CurentPos - 1:
            Neighbours.append([x + 1, y])
    
    #left
    if y >= 1:
        NeighbourLeft = num_data[x][y - 1]
        if NeighbourLeft >= CurentPos - 1:
            Neighbours.append([x, y - 1])
    #right
    row_length = len(num_data[0])
    if y < row_length - 1:
        NeighbourRight = num_data[x][y + 1]
        if NeighbourRight >= CurentPos - 1:
            Neighbours.append([x, y + 1])

    return Neighbours

#bfs
def bfs(start, part):
    depth = 0
    StopPosPart2 = []
    start.append(depth)
    Visited = []
    Queue = [start]
    while len(Queue) > 0:
        row, col, depth = Queue.pop(0)

        #if the current position holds 1, then make it a stop position for part 2
        if part == 2:
            temp = num_data[row][col]
            if temp == 1:
                StopPosPart2 = [row, col]

        Visited.append([row, col])

        #once it finds the StopPos - count depth
        if part == 1:
            if [row, col] == StopPosPart1:
                return depth
        elif part == 2:
            if [row, col] == StopPosPart2:
                return depth

        #returns list of neighbours
        if part == 1:
            around = NeighboursPart1(row,col)
        elif part == 2:
            around = neighboursPart2(row, col)

        #itirates over the list
        for row, col in around:
            if [row, col] not in Visited:
                if not any([row == r and col == c for r, c, _ in Queue]):
                    Queue.append([row, col, depth + 1])
    return 0

print('Part1: ', bfs(StartPosPart1, 1)) #part1
print('Part2: ', bfs(StartPosPart2, 2)) #part2