from random import randint, choice

x = 0
y = 0

class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.space = [] # or initialize it with walls using get_walls()

def draw_grid(graph, width=1):
    for y in range(graph.height):
        for x in range(graph.width):
            if (x, y) in graph.space:
                print("%%-%ds" % width % '.', end="")
            else:
                print("%%-%ds" % width % '#', end="")
        print()

def randomWalk(steps):
    x = 25  # Make sure you initialize the position to 0,0 each time the function is called
    y = 25
    out = []
    directions = ['N', 'E', 'S', 'W']  # To keep track of directions, you could use strings instead of 0, 1, 2, 3.
    for i in range(steps):
        a = choice(directions)  # You can use random.choice to choose a dir
        if a == 'N':
            y += 1
        elif a == 'S':
            y -= 1
        elif a == 'E':
            x += 1
        else:
            x -= 1

        out.append((x, y))
    return out 


def main():
    g = MapGrid(50, 50)
    g.space = randomWalk(500)
    draw_grid(g)
    x = input()
    main()

if __name__ == '__main__':
    main()
