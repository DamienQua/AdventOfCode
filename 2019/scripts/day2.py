# https://adventofcode.com/2019/day/2
# --- Day 2: 1202 Program Alarm ---

# Part 1 :
integers = list(map(int, open("inputs/day2.txt").read().split(",")))
integers[1], integers[2] = 12, 2
for i in range(3, len(integers), 4) :
    if integers[i-3] == 1 :
        integers[integers[i]] = integers[integers[i-2]] + integers[integers[i-1]]
    if integers[i-3] == 2 :
        integers[integers[i]] = integers[integers[i-2]] * integers[integers[i-1]]
print("Value at position 0 : ", integers[0])

# Part 2 :
for noun in range(100) :
    for verb in range(100) :
        integers = list(map(int, open("inputs/day2.txt").read().split(",")))
        integers[1], integers[2] = noun, verb
        for i in range(3, len(integers), 4) :
            if integers[i-3] == 1 :
                integers[integers[i]] = integers[integers[i-2]] + integers[integers[i-1]]
            if integers[i-3] == 2 :
                integers[integers[i]] = integers[integers[i-2]] * integers[integers[i-1]]
            if integers[i-3] == 99 :
                break
        if(integers[0] == 19690720):
            print("100 * noun + verb : ", 100*noun+verb)
            break