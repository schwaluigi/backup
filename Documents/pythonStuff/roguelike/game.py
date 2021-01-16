import curses
from curses import wrapper
from random import randint

# REMEMBER that in curses position, such as in addstr or addch, is (y, x)

SCREEN_WIDTH= 100
SCREEN_HEIGHT = 40

MAP_WIDTH = 80
MAP_HEIGHT = 35

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30


class Tile:
    #a tile of the map and its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
 
        #by default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight


class Rect:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
 
    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        #returns true if this rectangle intersects with another one
       return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


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
        stdscr.addch(self.y, self.x, self.char, self.color)
 
    def clear(self, stdscr):
        #erase the character that represents this object
        stdscr.addch(self.y, self.x, ' ', self.color)


def create_room(room):
    global my_map
    #go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            my_map[x][y].blocked = False
            my_map[x][y].block_sight = False

def create_h_tunnel(x1, x2, y):
    global my_map
    for x in range(min(x1, x2), max(x1, x2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False

def create_v_tunnel(y1, y2, x):
    global my_map
    #vertical tunnel
    for y in range(min(y1, y2), max(y1, y2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False

def make_map(player, objects):
    global my_map
 
    #fill map with "blocked" tiles
    my_map = [[ Tile(True) for y in range(MAP_HEIGHT) ] for w in range(MAP_WIDTH) ]

    rooms = []
    num_rooms = 0
 
    for r in range(MAX_ROOMS):
        #random width and height
        w = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        #random position without going out of the boundaries of the map
        x = randint(0, MAP_WIDTH-w-1)
        y = randint(0, MAP_HEIGHT-h-1)
        
        #"Rect" class makes rectangles easier to work with
        new_room = Rect(x, y, w, h)
 
        #run through the other rooms and see if they intersect with this one
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            #this means there are no intersections, so this room is valid
 
            #"paint" it to the map's tiles
            create_room(new_room)
 
            #center coordinates of new room, will be useful later
            (new_x, new_y) = new_room.center()
            
            if num_rooms == 0:
                #this is the first room, where the player starts at
                player.x = new_x
                player.y = new_y

            else:
                #all rooms after the first:
                #connect it to the previous room with a tunnel
 
                #center coordinates of previous room
                (prev_x, prev_y) = rooms[num_rooms-1].center()
 
                #draw a coin (random number that is either 0 or 1)
                if randint(0, 1):
                    #first move horizontally, then vertically
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    #first move vertically, then horizontally
                    create_v_tunnel(prev_y, new_y, prev_x)
                    create_h_tunnel(prev_x, new_x, new_y)
 
            #finally, append the new room to the list
            rooms.append(new_room)
            num_rooms += 1

def render_all(stdscr, objects):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = my_map[x][y].block_sight
            if wall:
                stdscr.addch(y, x, '#', curses.color_pair(0))
            else:
                stdscr.addch(y, x, '.', curses.color_pair(1) | curses.A_BOLD)
    #draw all objects in the list
    for obj in objects:
        obj.draw(stdscr)

def handle_keys(stdscr, objects, player):
    user_input = stdscr.getch() 
     
    for obj in objects:
        obj.clear(stdscr)
        
    if user_input == ord('r'):
        main(stdscr)
    
    elif user_input == ord('q'):
        return True

    #movement keys
    elif user_input == curses.KEY_UP:
        player.move(0, -1) 

    elif user_input == curses.KEY_DOWN:
        player.move(0, 1)
    
    elif user_input == curses.KEY_LEFT:
        player.move(-1, 0)
    
    elif user_input == curses.KEY_RIGHT:
        player.move(1, 0)
        

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    player = GameObject(SCREEN_HEIGHT//2, SCREEN_WIDTH//2, '@', curses.color_pair(0) | curses.A_BOLD)
    npc = GameObject(SCREEN_HEIGHT//2 + 5, SCREEN_WIDTH//2 - 15, '@', curses.color_pair(0) | curses.A_BOLD)
    objects = [player]
    make_map(player, objects)
    curses.curs_set(0)
    stdscr.erase()
    while True:

        render_all(stdscr, objects)

        stdscr.refresh()
        exit_game = handle_keys(stdscr, objects, player)
        if exit_game:
            break

wrapper(main)
