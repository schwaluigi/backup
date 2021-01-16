import curses
from curses import wrapper

# REMEMBER>> position, such as in addstr or addch, is y, x

SCREEN_WIDTH= 40
SCREEN_HEIGHT = 20

MAP_WIDTH = 40
MAP_HEIGHT = 20

class GameObject:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, y, x, char, color):
        self.y = y
        self.x = x
        self.char = char
        self.color = color
 
    def move(self, dy, dx):
        #move by the given amount
        if not my_map[self.y + dy][self.x + dx].blocked:
            self.y += dy
            self.x += dx
 
    def draw(self, stdscr):
        #draw the character that represents this object at its position
        stdscr.addch(self.y, self.x, self.char, self.color)
 
    def clear(self, stdscr):
        #erase the character that represents this object
        stdscr.addch(self.y, self.x, ' ', self.color)


class Tile:
    #a tile of the map and its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
 
        #by default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

def make_map():
    global my_map
 
    my_map = [[Tile(False) for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    
    my_map[19][39].blocked = True
    my_map[19][39].block_sight = True
    my_map[5][2].blocked = True
    my_map[5][2].block_sight = True

def render_all(stdscr, objects):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = my_map[y][x].block_sight
            if wall:
                stdscr.addch(y, x, '#', curses.color_pair(0))
            else:
                stdscr.addch(y, x, '.', curses.color_pair(0))
    #draw all objects in the list
    for obj in objects:
        obj.draw(stdscr)


def handle_keys(stdscr, objects, player):
    user_input = stdscr.getch() 
     
    for obj in objects:
        obj.clear(stdscr)
        
    #movement keys
    if user_input == curses.KEY_UP:
        player.move(-1, 0) 

    elif user_input == curses.KEY_DOWN:
        player.move(1, 0)
    
    elif user_input == curses.KEY_LEFT:
        player.move(0, -1)
    
    elif user_input == curses.KEY_RIGHT:
        player.move(0, 1)
        
    elif user_input == ord('q'):
        return True




def main(stdscr):
    player = GameObject(SCREEN_HEIGHT//2, SCREEN_WIDTH//2, '@', curses.color_pair(0) | curses.A_BOLD)
    npc = GameObject(SCREEN_HEIGHT//2 - 5, SCREEN_WIDTH//2, '@', curses.color_pair(0))
    objects = [npc, player]
    make_map()
    curses.curs_set(0)
    stdscr.erase()
    while True:

        render_all(stdscr, objects)

        stdscr.refresh()
        exit_game = handle_keys(stdscr, objects, player)
        if exit_game:
            break


wrapper(main)
