# https://adventofcode.com/2019/day/1
# --- Day 1: The Tyranny of the Rocket Equation ---

# Part 1 :
modules = list(map(int, open("inputs/day1.txt").read().split("\n")[:-1]))
fuels = [module//3-2 for module in modules]
print("Sum of the fuel requirements : ", sum(fuels))

# Part 2 :
fuels = []
for module in modules :
    fuel = module//3-2
    while fuel > 0 :
        fuel_tmp = fuel
        fuel = fuel//3 - 2
        fuels.append(fuel_tmp)
print("Sum of the fuel requirements : ", sum(fuels))