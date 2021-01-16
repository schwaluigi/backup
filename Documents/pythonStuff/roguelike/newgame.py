import curses
from curses import wrapper
from random import choice, randint

# MIGHT HAVE TO REMAKE TO IMPLEMENT SCROLLING CAMERA
# HAH, I DIDN'T NEED TO REMAKE TO USE A SCROLLING CAMERA, LOSER.

# REMEMBER>> position, such as in addstr or addch, is y, x

# # # # # # # # # # # #
#stdscr.addstr(SCREEN_HEIGHT, 0, 'YOU DIPSHIT! You fell!')
# # # # # # # # # # # #


SCREEN_WIDTH = 60
SCREEN_HEIGHT = 30

MAP_WIDTH = 120
MAP_HEIGHT = 60

WALL_CH = '#'
GROUND_CH = '.'

class GameObject:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
 
    def move(self, dx, dy):
        #move by the given amount
        if not my_map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self, stdscr):
        #draw the character that represents this object at its position
        (x, y) = to_camera_coordinates(self.x, self.y)
        if x is not None:
            stdscr.addch(int(y), int(x), self.char, self.color)

    def clear(self, stdscr):
        (x, y) = to_camera_coordinates(self.x, self.y)
        if x is not None:
            #erase the character that represents this object
            stdscr.addch(int(y), int(x), ' ', self.color)


class Tile:
    #a tile of the map and its properties
    def __init__(self, blocked, exit):
        self.blocked = blocked
        self.exit = exit

def make_map(stdscr, player, objects, steps):
    global my_map
 
    #fill map with "blocked" tiles
    my_map = [[ Tile(True, False)
        for y in range(MAP_HEIGHT)]
            for x in range(MAP_WIDTH)]
 
    x = MAP_WIDTH//2  # Make sure you initialize the position to 0,0 each time the function is called    
    y = MAP_HEIGHT//2
    player.x = x
    player.y = y

    directions = ['N', 'E', 'S', 'W']  # To keep track of directions, you could use strings instead of 0, 1, 2, 3.    
    for i in range(steps):
        a = choice(directions)  # You can use random.choice to choose a dir    
        if a == 'N':
            y += 1
        elif a == 'E':
            x += 1  
        elif a == 'S':
            y -= 1
        else:
            x -= 1

        if x < MAP_WIDTH-2 and x > -1 and y < MAP_HEIGHT-2 and y > -1:
            my_map[x][y].blocked = False 
            my_map[x][y].exit = False

    try:
        if my_map[x][y].blocked == True:
            make_map(stdscr, player, objects, steps)
        else:
            my_map[x][y].exit = True
    except:
        make_map(stdscr, player, objects, steps)

    my_map[player.x][player.y].blocked = False

    (camera_x, camera_y) = (player.x, player.y)

def move_camera(target_x, target_y):
    global camera_x, camera_y
 
    #new camera coordinates (top-left corner of the screen relative to the map)
    x = target_x - SCREEN_WIDTH / 2  #coordinates so that the target is at the center of the screen
    y = target_y - SCREEN_HEIGHT / 2
 
    #make sure the camera doesn't see outside the map
    if x < 0: x = 0
    if y < 0: y = 0
    if x > MAP_WIDTH - SCREEN_WIDTH - 1: x = MAP_WIDTH - SCREEN_WIDTH - 1
    if y > MAP_HEIGHT - SCREEN_HEIGHT - 1: y = MAP_HEIGHT - SCREEN_HEIGHT - 1
 
    (camera_x, camera_y) = (x, y)
 
def to_camera_coordinates(x, y):
    #convert coordinates on the map to coordinates on the screen
    (x, y) = (x - camera_x, y - camera_y)
 
    if (x < 0 or y < 0 or x >= SCREEN_WIDTH or y >= SCREEN_HEIGHT):
        return (None, None)  #if it's outside the view, return nothing
 
    return (x, y)

def render_all(stdscr, objects, player):
    move_camera(player.x, player.y)
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            (map_x, map_y) = (camera_x + x, camera_y + y)
            wall = my_map[int(map_x)][int(map_y)].blocked
            exit = my_map[int(map_x)][int(map_y)].exit
            if exit:
                stdscr.addch(y, x, 'O', curses.color_pair(0) | curses.A_BOLD)
            elif wall:
                stdscr.addch(y, x, WALL_CH, curses.color_pair(2) | curses.A_BOLD)
            else:
                stdscr.addch(y, x, GROUND_CH, curses.color_pair(2) | curses.A_BOLD)
    
    #draw all objects in the list
    for obj in objects:
        obj.draw(stdscr)
    
def handle_keys(stdscr, objects, player, steps):
    user_input = stdscr.getch() 
     
    for obj in objects:
        obj.clear(stdscr)
        
    #movement keys
    if user_input == curses.KEY_UP or user_input == ord('k'):
            player.move(0 ,-1) 
    elif user_input == curses.KEY_DOWN or user_input == ord('j'):
        player.move(0 ,1)
    elif user_input == curses.KEY_LEFT or user_input == ord('h'):
        player.move(-1 ,0)
    elif user_input == curses.KEY_RIGHT or user_input == ord('l'):
        player.move(1, 0)
    
    elif user_input == ord('y'):
        player.move(-1, -1)
    elif user_input == ord('u'):
        player.move(1, -1)
    elif user_input == ord('b'):
        player.move(-1, 1)
    elif user_input == ord('n'):
        player.move(1, 1)
    
    elif user_input == ord(' ') and my_map[player.x][player.y].exit:
        make_map(stdscr, player, objects, steps)

    #not movement. wow.
    elif user_input == ord('q'):
        return True

    elif user_input == ord('r'):
        main(stdscr)

    if user_input == ord('K'): 
        while not my_map[player.x + 0][player.y + -1].blocked:
            player.move(0, -1) 
    elif user_input == ord('J'):
        while not my_map[player.x + 0][player.y + 1].blocked:
            player.move(0, 1)
    elif user_input == ord('H'):
        while not my_map[player.x + -1][player.y + 0].blocked:
            player.move(-1, 0)
    elif user_input == ord('L'):
        while not my_map[player.x + 1][player.y + 0].blocked:
            player.move(1, 0)

    elif user_input == ord('Y'):
        while not my_map[player.x + -1][player.y + -1].blocked:
            player.move(-1, -1)
    elif user_input == ord('U'):
        while not my_map[player.x + 1][player.y + -1].blocked:
            player.move(1, -1)
    elif user_input == ord('B'):
        while not my_map[player.x + -1][player.y + 1].blocked:
            player.move(-1, 1)
    elif user_input == ord('N'):
        while not my_map[player.x + 1][player.y + 1].blocked:
            player.move(1, 1)

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    player = GameObject(0, 0, '@', curses.color_pair(0) | curses.A_BOLD)
    npc = GameObject(MAP_HEIGHT//2 - 5, MAP_WIDTH//2, '@', curses.color_pair(0))
    objects = [player]
    steps = int((MAP_WIDTH*MAP_HEIGHT)/randint(10,15))
    make_map(stdscr, player, objects, steps)
    while True:

        render_all(stdscr, objects, player)

        stdscr.refresh()
        exit_game = handle_keys(stdscr, objects, player, steps)
        if exit_game:
            break


wrapper(main)
