from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def next_path(starting_room, all_rooms=set()):
    visited = set()

    for room in all_rooms:  # for our rooms in our graph
        visited.add(room) # add first room to out set()
        path = [] # empty list that will be appended with out path
        opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'} # directions we can move in the graph

        def add_to_path(r, back_to=None):
            visited.add(r) # visited room is assigned to out set()
            exits = r.get_exits() # exit variable to allow us to call when we want to exit a room/node

            for direction in exits:
                # print(direction)
                if r.get_room_in_direction(direction) not in visited: # if a room has not been visited too
                    path.append(direction) # append to that direction to find the room that has not beene visited yet
                    add_to_path(r.get_room_in_direction(direction), opposite[direction]) # our funciotn will reloop beacuse of the our recursive call and we are getting n, s, e, w directions 


            if back_to: # if the room is None
                path.append(back_to) # back track in our path to our next path

        add_to_path(starting_room) # go back on our graph to the next branch of the graph and go through the process again

        return path # return our path


def create_path(starting_room, visited=set()):
    path = []
    opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'} # directions we can move in the graph

    def add_to_path(room, back_to=None):
        visited.add(room)  # visited room is assigned to out set()
        exits = room.get_exits() # exit variable to allow us to call when we want to exit a room/node
        path_length = {} # to get the amount of rooms. Note: set key == direction and value == the len() of the rooms we've looped through
        traverse_order = [] 

        # print("show traverse order as empty", traverse_order)

        for direction in exits:
            # print(direction)
            path_length[direction] = len(next_path(room.get_room_in_direction(direction), visited)) # for every direction that goes into the room we are going to check the path len() and put the direction into our path_length. Then we will call next_path recurslily to get the all of the possible directions we can go then we call visited to to see all the room we have visited and take them out of the possible directions we can go


        for key, value in sorted(path_length.items(), key=lambda val: val[1]): # we are looping through the key and value and creating an anonymous funciton and that annnymous is going to go through our path and sort the len() of all the rooms  
            # print("this is the len of our path", key, value)
            print(key, value) # print key so we can see our direction and the len of the graph we are in
            traverse_order.append(key) # adding the direction I'm going to the traverse_order list

            # print(" my traverse order list", traverse_order)

        for direction in traverse_order: # loop through the direcitons in the traverse order list
            # print(direction)
            if room.get_room_in_direction(direction) not in visited: # if a room has not been visited too
                path.append(direction) # append to that direction to find the room that has not beene visited yet
                add_to_path(room.get_room_in_direction(direction), opposite[direction]) # our funciotn will reloop beacuse of the our recursive call and we are getting n, s, e, w directions 

        if len(visited) == len(world.rooms): # if the len() of the rooms we've been too is equal to the rooms in the graph
            return 
        elif back_to: # else if the room is None
            path.append(back_to) # back track in our path to our next path

    add_to_path(starting_room) # go back on our graph to the next branch of the graph and go through the process again

    return path # return our path


traversal_path = create_path(world.starting_room) # we are recursivly calling our funciton so we can repeat the process and move back to our starting_room/node




# Do not touch what's other it's just test's
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
