# https://adventofcode.com/2019/day/3
# --- Day 3: Crossed Wires ---
def set_coords(x0, y0, x, y, history, dir) :
    if dir == "R" :
        for a in range(x0, x+1) :
            history.add((a, y0))
    if dir == "L" :
        for a in range(x, x0+1) :
            history.add((a, y0))
    if dir == "U" :
        for b in range(y0, y+1) :
            history.add((x0, b))
    if dir == "D" :
        for b in range(y, y0+1) :
            history.add((x0, b))
    return history

def positions(wire) :
    x, y = 0, 0
    history = set()
    history.add((x, y))
    for dir in wire :
        x0, y0 = x, y
        if dir[0] == "R" :
            x += int(dir[1:])
        if dir[0] == "L" :
            x -= int(dir[1:])
        if dir[0] == "U" :
            y += int(dir[1:])
        if dir[0] == "D" :
            y -= int(dir[1:]) 
        set_coords(x0, y0, x, y, history, dir[0])
    return history

# Part 1 :
wires = open("inputs/day3.txt").read().split("\n")[:-1]
paths = [sorted(positions(list(map(str, wires[i].split(","))))) for i in range(len(wires))]
intersect = set(paths[0]).intersection(paths[1]).difference([(0,0)])
distance = min([abs(i[0]) + abs(i[1]) for i in intersect])
print("Minimum Manhattan distance :", distance)

# Part 2 :
steps = 2 + min([sum(wire.index(inter) for wire in paths) for inter in intersect])
print("Fewest steps to reach an intersection : ", steps)