from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# our Stack for our dft
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# our Queue for our bfs
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


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

# *** understand ***
# I need to to find the current room
# I am going to use depth-first traversal (dft) to iterate through our rooms 
# Once we hit a node with a dead end I want to pop() of the top of the stack wwitch are the nodes that have already been loop through back to the begining of the stack (the first node I loop through) 
# I want to find the closes room that hasn’t been iterate through using bfs from that first node (the current node we are on)

# *** Plan ***
# Create a dft function 
# Create a stack to add our nodes that are being iterated through into
# Push our starting node since we've been to it into the stack
# create a variable called visited and assign set() to it so we can call visited nodes
# Loop through our stack = ps: the nodes that are being iterated through 
# creating a varibale called current_node so once we are on our current node we can pop() it from our stack
# 

def dft(self, starting_node):
    stack = Stack() 
    
    stack.push(starting_node)

    visited = set()

    while stack.size > 0:
        current_node = stack.pop()

        if current_node not in visited:









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
