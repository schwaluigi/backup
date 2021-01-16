rooms = [[0, 'Start', ['stick', 'leaf']], [1, 'Cliff', ['rock', 'boulder']]]
pos = 0

def print_info(rooms, pos):
    for room in rooms:
        if room[0] == pos:
            print('---')
            print('Room:\n{}\n\nItems: '.format(room[1]), end='')
            for item in room[2]:
                print('\n{}'.format(item), end='')
            print('\n---')

print_info(rooms, pos)
