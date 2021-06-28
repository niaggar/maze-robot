"""
1. Siempre tener un muro a la derecha.
2. Si no hay muro girar a la derecha.
3. Si hay muro a la derecha y al frente girar a la izquierda hasta que no haya muro.
4. Recorrer todo el laberinto hasta volver al punto inicial siguiendo las anteriores reglas.
"""


maze = []
rb_pos = []
rb_pos_start = []


def print_map():
    global maze
    print('-' * 15)

    for y in range(len(maze[0])):
        row = ''
        for x in maze:
            row += f'{str(x[y])} '
        print(row)

    print('-' * 15)


def create_maze():
    global maze, rb_pos, rb_pos_start

    print('# filas -- # columnas')
    maze_size = [int(x) for x in input().split()]

    print('write the column')
    for y in range(maze_size[1]):
        txt_column = list(input())
        if len(txt_column) == maze_size[0]:
            column = [[int(y), 0] for y in txt_column]
            maze.append(column)

    print_map()

    print('Robot position: # X -- # Y')
    rb_pos_start = [int(x) for x in input().split()]

    maze[rb_pos_start[0]][rb_pos_start[1]][0] = 2

    rb_pos = rb_pos_start.copy()
    rb_pos.append('N')


def directions(direction):
    list_direction = {
        'N': {
            'F': 'N',
            'R': 'E',
            'L': 'W',
            'B': 'S',
        },
        'E': {
            'F': 'E',
            'R': 'S',
            'L': 'N',
            'B': 'W',
        },
        'S': {
            'F': 'S',
            'R': 'W',
            'L': 'E',
            'B': 'N',
        },
        'W': {
            'F': 'W',
            'R': 'N',
            'L': 'S',
            'B': 'E',
        },
    }
    return list_direction[direction]


def robot_calc_pos(rX, rY, direction, to):
    move = {
        'N': ( 0, -1),
        'S': ( 0,  1),
        'E': ( 1,  0),
        'W': (-1,  0),
    }
    list_direction = {
        'N': {
            'F': move['N'],
            'R': move['E'],
            'L': move['W'],
            'B': move['S'],
        },
        'E': {
            'F': move['E'],
            'R': move['S'],
            'L': move['N'],
            'B': move['W'],
        },
        'S': {
            'F': move['S'],
            'R': move['W'],
            'L': move['E'],
            'B': move['N'],
        },
        'W': {
            'F': move['W'],
            'R': move['N'],
            'L': move['S'],
            'B': move['E'],
        },
    }

    m = list_direction[direction][to]

    return rX + m[0], rY + m[1]


def robot_move():
    global maze, rb_pos

    rX = rb_pos[0]
    rY = rb_pos[1]
    direction = rb_pos[2] if rb_pos[2] else 'N'

    maze[rX][rY][0] = 0
    pts = directions(direction)

    walls = {
        'N': maze[rX][rY - 1][0] if rY - 1 >= 0 else 1,
        'E': maze[rX + 1][rY][0] if rX + 1 < len(maze) else 1,
        'S': maze[rX][rY + 1][0] if rY + 1 < len(maze[rX]) else 1,
        'W': maze[rX - 1][rY][0] if rX - 1 >= 0 else 1,
    }

    if walls[pts['R']]:
        if not walls[pts['F']]:
            rX, rY = robot_calc_pos(rX, rY, direction, 'F')
            direction = pts['F']

        elif not walls[pts['L']]:
            rX, rY = robot_calc_pos(rX, rY, direction, 'L')
            direction = pts['L']

        elif not walls[pts['B']]:
            rX, rY = robot_calc_pos(rX, rY, direction, 'B')
            direction = pts['B']

        else:
            print('I\'m locked')

    else:
        rX, rY = robot_calc_pos(rX, rY, direction, 'R')
        direction = pts['R']

    rb_pos[0] = rX
    rb_pos[1] = rY
    rb_pos[2] = direction

    maze[rX][rY][0] = 2
    maze[rX][rY][1] += 1


def main():
    global rb_pos, rb_pos_start

    create_maze()

    print_map()
    robot_move()
    print_map()

    while True:
        robot_move()
        print_map()

        if rb_pos[0] == rb_pos_start[0] and rb_pos[1] == rb_pos_start[1]:
            break


if __name__ == '__main__':
    main()
