from random import randint, choice
import os

class MapGrid:    
    def __init__(self, width, height):    
        self.width = width    
        self.height = height    
        self.walls = [] # or initialize it with walls using get_walls()
        self.player = (5, 5) 

    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d == 'd':
            pos = (x + 1, y)
        elif d == 'a':
            pos = (x - 1, y)
        elif d == 'w':
            pos = (x, y - 1)
        elif d == 's':
            pos = (x, y + 1)
        else:
           pos = (x, y) 

        if pos not in self.walls:
            self.player = pos


def draw_grid(graph, width=2):
    for y in range(graph.height):
            for x in range(graph.width):
                if (x, y) in graph.walls:
                    symbol = '#'
                elif (x, y) == graph.player:
                    symbol = '@'
                else:
                    symbol = '.'
                print("%%-%ds" % width % symbol, end="")
            print()

def get_walls(graph,wall_percent=.2):
    out = []
    for i in range(int(graph.height*graph.width*wall_percent)//2):
        x = randint(1, graph.width-1)
        y = randint(1, graph.height-2)
        # choice chooses between one of the given choices, so this
        # offsets the wall (or every other wall if /2 given in 
        # for loop) by a random amount in both directions
        out.append((x, y))
        out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))

    num = 1
    for i in range(int(graph.width)):
        x = graph.width-num
        y = graph.height-graph.height
        y2 = graph.height-1
        num += 1
        out.append((x, y))
        out.append((x, y2))
    num = 1
    for i in range(int(graph.height)):
        x = graph.height-num
        y = graph.width-graph.width
        y2 = graph.width-1
        num += 1
        out.append((y, x))
        out.append((y2, x))

    return out


def clear():
    
    for i in range(50):
        print(" ")

    # bad terminal flah if I actuall clear term,
    # so I'm just printing a bunch of lines for now
    # obviously this is a garbage solution.

    """
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')
    """

def main():
    clear()
    graph = MapGrid(30, 20)
    graph.walls = get_walls(graph)
    while True:
        draw_grid(graph)
        d = input("Move: (w), (a), (s), (d)\n> ").lower().strip()
        graph.move_player(d)
        clear() 
    print("You made it!")


if __name__ == '__main__':
    main()
