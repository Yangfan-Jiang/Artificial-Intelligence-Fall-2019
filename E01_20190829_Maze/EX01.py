# AI Experiment #1: Maze Problem
# 2019/8/29

__author__ = 'Yangfan Jiang (jiangyf29@mail2.sysu.edu.cn)'

'''Solver code of AI experiment #1: Uninformed Search
   Maze Problem (shorest path) by using BFS'''

def load_data(file_name, mode):
    '''
    Load data file
    
    Input:
    file_name (string): file name
    mode (int): 0 or 1, two types of data
    
    Returns:
    maze (2D list): 2D list represents a maze
    wall (char): character read from data file which represents wall
    '''
    line_cnt = 0
    if mode == 0:
        end = 18
        wall = '%'
        road = ' '
        
    elif mode == 1:
        end = 39
        wall = '1'
        road = '0'
    else:
        raise Exception('Bad Parameter')
        
    # 2D list represents a maze
    maze = []
    
    with open(file_name) as data:
        for line in data:
            if line_cnt == end:
                break
            if mode == 0 or line_cnt >= 21:
                maze.append(list(line))
            line_cnt += 1
    return maze, wall
    
def print_maze(maze):
    '''
    Maze data visualization, may helpful for debug
    '''
    for i in maze:
        print(''.join(i), end='')
    
def bfs(maze, start_pos, wall):
    '''
    Find the shorest path of maze by using Breadth-First
    
    maze (2D list): 2D list represents a maze
    start_pos (list): [x-axis, y-axis, trace], first and second element record
                      the current position of the state, third element record the 
                      walking trace(a list of strings)
    wall (char): a character represents wall
    
    Returns: None
    '''
    curr_len = 0
    x = start_pos[0]
    y = start_pos[1]
    frontier = [start_pos]
    #print_maze(maze)
    
    while frontier:
        new_frontier = []
        for next_pos in frontier:
            x = next_pos[0]
            y = next_pos[1]
            path = next_pos[2]
            
            if maze[x][y] == 'E':
                print('Shortest length:', curr_len)
                print('Path:')
                cnt = 0
                for i in next_pos[2]:
                    print(i,end=' ')
                    cnt += 1
                    if cnt % 10 == 0:
                        print()
                return
                
            maze[x][y] = wall
            if maze[x-1][y] != wall:
                new_frontier.append([x-1, y, path+['up']])
            if maze[x][y-1] != wall:
                new_frontier.append([x, y-1, path+['left']])
            if maze[x+1][y] != wall:
                new_frontier.append([x+1, y, path+['down']])
            if maze[x][y+1] != wall:
                new_frontier.append([x, y+1, path+['right']])
        frontier = new_frontier
        curr_len += 1
    
if __name__ == '__main__':
    maze_file = 'MazeData.txt'
    maze ,wall= load_data(maze_file, 1)
    start_pos = [1, 34, []]
    bfs(maze, start_pos, wall)

    
    