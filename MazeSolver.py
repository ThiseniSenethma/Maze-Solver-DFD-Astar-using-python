import random
import heapq
#To implment the priority queue

def startup():   #Asking the user which option he/she wants to choose to solve the maze
    print(""" Select one option 

                Enter 1 to solve the maze using DFS 

                Enter 2 to solve the maze using A* """)

    userInput = int(input("Enter number: "))

#According to his input the relv def func will run
    if userInput == 1:
        dfs_result = calc_using_dfs()
        print("DFS Visited Nodes:", dfs_result['visited_nodes'])
        print("DFS Final Path:", dfs_result['path'])
        print_maze(dfs_result['path'])
    elif userInput == 2:
        a_star_result = calc_using_a_star()
        print("A* Visited Nodes:", a_star_result['visited_nodes'])
        print("A* Final Path:", a_star_result['path'])
        print_maze(a_star_result['path'])
    else:
        print("Invalid Input  ! Please try again")
        startup()


    while True:
        user_choice = input("Do you want to solve the same maze using the other method? (y/n): ").lower()
        if user_choice == 'y':
            startup()
        elif user_choice == 'n':
            print("Exiting Program")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


#Initialixing a 2D array with all visited nodes
def calc_using_dfs():
    visited = [[False] * len(maze_grid[0]) for _ in range(len(maze_grid))]
    dfs_result = dfs(maze_grid, start, goal, visited)

#A dict with visited nodes and final path is returned
    return {
        'visited_nodes': dfs_result['visited_nodes'],
        'path': dfs_result['path']
    }

#DFS algorithm again return dict with visited nodes and final path
def dfs(maze, current, goal, visited):
    x, y = current

    # Checking if the current node is the goal
    if current == goal:
        return {'visited_nodes': [current], 'path': [current]}

    visited[x][y] = True

    # Checkng all possible moves in increasing order
    moves = [
        (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),  # horizontal and vertical
        (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)  # diagonal
    ]

    for move in moves:
        new_x, new_y = move
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#' and not visited[new_x][new_y]:
            path = dfs(maze, (new_x, new_y), goal, visited)
            if path['path']:  # Checking if a path is found
                return {'visited_nodes': [current] + path['visited_nodes'], 'path': [current] + path['path']}

    return {'visited_nodes': [current], 'path': []}  # No path found

#A* calculation - initializing 2D array with visited nodes
def calc_using_a_star():
    visited = [[False] * len(maze_grid[0]) for _ in range(len(maze_grid))]
    a_star_result = astar(maze_grid, start, goal, visited)

    return {
        'visited_nodes': a_star_result['visited_nodes'],
        'path': a_star_result['path']
    }

#calc the manhatton distance between 2 points and used in A* algo
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

#A* Algo - use priority queue to find the best and optimal path
def astar(maze, start, goal, visited):
    priority_queue = [(heuristic(start, goal), 0, start, [])]

    while priority_queue:
        _, cost, current, path = heapq.heappop(priority_queue)

        x, y = current
        if current == goal:
            return {'visited_nodes': path + [current], 'path': path + [current]}

        if not visited[x][y]:
            visited[x][y] = True

            # Check possible moves (up, down, left, right, and diagonals)
            moves = [
                (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)
            ]

            for move in moves:
                new_x, new_y = move
                if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#' and not \
                        visited[new_x][new_y]:
                    new_cost = cost + 1
                    priority = new_cost + heuristic((new_x, new_y), goal)
                    heapq.heappush(priority_queue, (priority, new_cost, (new_x, new_y), path + [current]))

    return {'visited_nodes': [], 'path': []}  # No path found

#Display maze
def print_maze(path=[]):
    for i in range(len(maze_grid)):
        for j in range(len(maze_grid[0])):
            if (i, j) == start:
                print('S', end=' ')
            elif (i, j) == goal:
                print('G', end=' ')
            elif (i, j) in path:
                print('●', end=' ')
            else:
                print(maze_grid[i][j], end=' ')
        print()


# Creating the maze 6x6 using a 2D arraylist
maze_size = (6, 6)
maze_grid = [['.' for _ in range(maze_size[1])] for _ in range(maze_size[0])]

# Randomly select start in range 0-11
start = (random.randint(0, 5), random.randint(0, 1))

# Randomly select goal in range 24-35
goal = (random.randint(0, 5), random.randint(4, 5))

# Selecting random 4 barriers
barriersList = []
while len(barriersList) < 4:
    barrier = (random.randint(0, 5), random.randint(0, 5))
    if barrier != start and barrier != goal and barrier not in barriersList:
        barriersList.append(barrier)

# Updating the maze with all the selected start, goal, and barrier nodes
maze_grid[start[0]][start[1]] = "S"
maze_grid[goal[0]][goal[1]] = "G"
for barrier in barriersList:
    maze_grid[barrier[0]][barrier[1]] = "#"

print("Original Maze:")
print_maze()

startup()
