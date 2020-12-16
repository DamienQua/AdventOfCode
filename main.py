import math
import os
import random
import re
import sys
from operator import itemgetter
from collections import defaultdict, deque

def word_count(str, letter):
    counts = dict()
    words = str

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts[letter] if letter in counts else 0

def find_trees(r, d, input) :
    tree = 0
    start = d
    slope = r
    for i in range(start, len(input), d):
        if input[i][r%len(input[i])] == "#" :
            tree += 1
        r += slope
    print("Number of trees X : ", tree)
    return tree

def find_valid_passport(tab, fields) :
    cptOK = 0
    l = ("g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    e = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    for field in fields :
        for ind in range(len(tab)):
            if field == "byr" and tab[ind][0] == field and 1920<=int(tab[ind][1])<=2020 :
                cptOK += 1
                break
            if field == "iyr" and tab[ind][0] == field and 2010<=int(tab[ind][1])<=2020 :
                cptOK += 1
                break
            if field == "eyr" and tab[ind][0] == field and 2020<=int(tab[ind][1])<=2030 :
                cptOK += 1
                break
            if field == "hgt" and tab[ind][0] == field :
                if "cm" in tab[ind][1] :
                    if 150<=int(tab[ind][1].split("cm")[0])<=193 :
                        cptOK += 1
                        break
                if "in" in tab[ind][1] :
                    if 59<=int(tab[ind][1].split("in")[0])<=76 :
                        cptOK += 1
                        break
            if field == "hcl" and tab[ind][0] == field and tab[ind][1][0] == "#" :
                if len(tab[ind][1][1:]) == 6 :
                    if tab[ind][1][1:] not in l :
                        cptOK += 1
                        break
            if field == "ecl" and tab[ind][0] == field : 
                if tab[ind][1] in e :
                    cptOK += 1
                    break
            if field == "pid" and tab[ind][0] == field and len(tab[ind][1]) == 9 :
                cptOK += 1
                break
    return 1 if cptOK == 7 else 0


def contestResponse1(input):
    valid, cpt, ok = 0, 0, 0
    s1 = []
    s2 = []
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for i in range(len(input)):
        for field in fields :
            if field in input[i] :
                cpt += 1
        if cpt == len(fields) or (cpt == len(fields)-1 and "cid" not in input[i]):
            ok = 1
        if ok == 1 :
            s = input[i].split("\n")
            for j in range(len(s)) :
                s1.append(s[j].split())
            for k in range(len(s1)) :
                for l in range(len(s1[k])):
                    s2.append(s1[k][l].split(":"))
            valid += find_valid_passport(s2, fields)
            s1.clear()
            s2.clear()
        ok = 0
        cpt = 0
    print("Valid passports : ", valid)
    return 

def findID(data):
    rowMin, rowMax = 0, 127
    colMin, colMax = 0, 7
    rows, cols = 0, 0
    row, col = 0, 0
    for i in range(len(data)):
        if i < 7 :
            rows = rowMax-rowMin
            if data[i] == 'F' :
                rowMax -= round(rows/2)
                if i == 6 :
                    row = min(rowMin, rowMax)
            if data[i] == 'B' :
                rowMin += round(rows/2)
                if i == 6 :
                    row = max(rowMin, rowMax)
        else :
            cols = colMax-colMin
            if data[i] == 'L' :
                colMax -= round(cols/2)
                if i == len(data)-1 :
                    col = min(colMin, colMax)
            if data[i] == 'R' :
                colMin += round(cols/2)
                if i == len(data)-1 :
                    col = max(colMin, colMax)
    return row*8+col

def word_count(str):
    counts = dict()
    words = str

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def day10(input):
    last_25_sum = []
    input = list(map(int, input))
    for i in range(len(input)) :
        for x in range(i, 25+i) :
            for y in range(i, 25+i) :
                last_25_sum.append(input[x]+input[y])
        last_25_sum_set = set(map(str, last_25_sum))
        if str(input[i+25]) not in last_25_sum_set :
            illegal = input[i+25]
            print("First number not to be a sum of 25 before it : ", illegal)
            break
        last_25_sum = []
    contiguous = []
    somme = 0
    cpt = 0
    ok = True
    while ok :
        contiguous.append(input[i])
        somme += input[i]
        i+=1
        if somme > illegal :
            somme = 0
            cpt += 1
            i = cpt
            contiguous = []
        if somme == illegal :
            ok = False
            print("Max : "+str(max(contiguous))+" Min : "+str(min(contiguous)))
            print("Max + Min : ", max(contiguous)+min(contiguous))

def day10 (input) :
    jolts = list(map(int, input))
    jolts.append(0)
    jolts.append(max(jolts)+3)
    jolts = sorted(jolts)
    outlet = 0
    nb_one, nb_two, nb_three = 0, 0, 0
    for i in range(1, len(jolts)) :
        if jolts[i] == jolts[i-1] + 1 :
            nb_one += 1
        if jolts[i] == jolts[i-1] + 2 :
            nb_two += 1
        if jolts[i] == jolts[i-1] + 3 :
            nb_three += 1
    print("Product of one by three : ", nb_one*nb_three)
    adapters = list(map(int, input))
    adapters.sort()
    cache = [0,0,1] + [0] * adapters[-1]
    for a in adapters:
        # a=1 corresponds to cache[3], so +2
        i = a + 2
        cache[i] = sum(cache[i-3:i])
    print(cache[-1])

def find_neighbors(tab, i, j) :
    cpt_seat, cpt_empty, cpt_floor = 0, 0, 0
    cpt = 0
    if tab[i][j] != "." :
        if i != 0 :
            if j == 0 :
                if i != len(tab)-1 : 
                    for x in range(i-1, i+2) :
                        for y in range(j, j+2) :
                            if not(x == i and y == j) :
                                if tab[x][y] == "L" :
                                    cpt_empty += 1
                                elif tab[x][y] == "#" :
                                    cpt_seat += 1
                                else : 
                                    cpt_floor += 1
                                cpt += 1
                else :
                    for x in range(i-1, i+1) :
                        for y in range(j, j+2) :
                            if not(x == i and y == j) :
                                if tab[x][y] == "L" :
                                    cpt_empty += 1
                                elif tab[x][y] == "#" :
                                    cpt_seat += 1
                                else : 
                                    cpt_floor += 1
                                cpt += 1

            elif j == len(tab[0])-1:
                if i != len(tab)-1 :
                    for x in range(i-1, i+2) :
                        for y in range(j-1, j+1) :
                            if not(x == i and y == j) :
                                if tab[x][y] == "L" :
                                    cpt_empty += 1
                                elif tab[x][y] == "#" :
                                    cpt_seat += 1
                                else : 
                                    cpt_floor += 1
                                cpt += 1
                else :
                    for x in range(i-1, i+1) :
                        for y in range(j-1, j+1) :
                            if not(x == i and y == j) :
                                if tab[x][y] == "L" :
                                    cpt_empty += 1
                                elif tab[x][y] == "#" :
                                    cpt_seat += 1
                                else : 
                                    cpt_floor += 1
                                cpt += 1
            else :
                if i != len(tab)-1 :
                    for x in range(i-1, i+2) :
                        for y in range(j-1, j+2) :
                            if not(x == i and y == j) :
                                if tab[x][y] == "L" :
                                    cpt_empty += 1
                                elif tab[x][y] == "#" :
                                    cpt_seat += 1
                                else : 
                                    cpt_floor += 1
                                cpt += 1
                else :
                    for x in range(i-1, i+1) :
                        for y in range(j-1, j+2) :
                            if not(x == i and y == j) :
                                if tab[x][y] == "L" :
                                    cpt_empty += 1
                                elif tab[x][y] == "#" :
                                    cpt_seat += 1
                                else : 
                                    cpt_floor += 1
                                cpt += 1
        else :
            if j == 0 :
                for x in range(i, i+2) :
                    for y in range(j, j+2) :
                        if not(x == i and y == j) :
                            if tab[x][y] == "L" :
                                cpt_empty += 1
                            elif tab[x][y] == "#" :
                                cpt_seat += 1
                            else : 
                                cpt_floor += 1
                            cpt += 1
            elif j == len(tab[0])-1 :
                for x in range(i, i+2) :
                    for y in range(j-1, j+1) :
                        if not(x == i and y == j) :
                            if tab[x][y] == "L" :
                                cpt_empty += 1
                            elif tab[x][y] == "#" :
                                cpt_seat += 1
                            else : 
                                cpt_floor += 1
                            cpt += 1
            else :
                for x in range(i, i+2) :
                    for y in range(j-1, j+2) :
                        if not(x == i and y == j) :
                            if tab[x][y] == "L" :
                                cpt_empty += 1
                            elif tab[x][y] == "#" :
                                cpt_seat += 1
                            else : 
                                cpt_floor += 1
                            cpt += 1
    else :
        return tab[i][j]
        
    if cpt_seat >= 5 :
        return "L"
    elif cpt_empty == cpt - cpt_floor :
        return "#"
    else :
        return tab[i][j]
    


def day11(input) :
    seats = []
    plane = []
    new_plane = []
    temp_plane = []
    nbSeats = 0
    for i in range(len(input)) :
        for j in range(len(input[0])) :
            seats.append(input[i][j])
        plane.append(seats)
        temp_plane = plane
        seats = []
    while True :
        for i in range(len(plane)) :
            for j in range(len(plane[0])) :
                seats.append(find_neighbors(temp_plane, i, j))
            new_plane.append(seats)
            seats = []
        if temp_plane == new_plane :
            for i in range(len(temp_plane)) :
                for j in range(len(temp_plane[0])) :
                    if temp_plane[i][j] == "#" :
                        nbSeats += 1
            print("Occupied seats : ", nbSeats)
            break 
        else :
            temp_plane = new_plane
            new_plane = []

def day12(input) :
    #Part one
    distance = [0, 0]
    degrees = 90
    for i in range(len(input)) :
        if input[i][0] == "N" :
            distance[0] += int(input[i][1:])
        elif input[i][0] == "S" :
            distance[0] -= int(input[i][1:])
        elif input[i][0] == "E" :
            distance[1] += int(input[i][1:])
        elif input[i][0] == "W" :
            distance[1] -= int(input[i][1:])
        elif input[i][0] == "L" :
            degrees -= int(input[i][1:])
        elif input[i][0] == "R" :
            degrees += int(input[i][1:])
        else :# "F"
            if degrees%360 == 0 :
                distance[0] += int(input[i][1:])
            elif degrees%360 == 90 :
                distance[1] += int(input[i][1:])
            elif degrees%360 == 180 :
                distance[0] -= int(input[i][1:])
            else : #270°
                distance[1] -= int(input[i][1:])
    print("P1 : Distance : ", abs(distance[0])+abs(distance[1]))  

    #Part two
    ship = [1, 10]
    distance = [0, 0]
    for i in range(len(input)) :
        if input[i][0] == "N" :
            ship[0] += int(input[i][1:])
        elif input[i][0] == "S" :
            ship[0] -= int(input[i][1:])
        elif input[i][0] == "E" :
            ship[1] += int(input[i][1:])
        elif input[i][0] == "W" :
            ship[1] -= int(input[i][1:])
        elif input[i][0] == "R" :
            if int(input[i][1:]) == 90 :
                ship[0], ship[1] = -ship[1], ship[0] 
            elif int(input[i][1:]) == 180 :
                ship[0], ship[1] = -ship[0], -ship[1]
            else : #270°
                ship[0], ship[1] = ship[1], -ship[0]

        elif input[i][0] == "L" :
            if int(input[i][1:]) == 90 :
                ship[0], ship[1] = ship[1], -ship[0] 
            elif int(input[i][1:]) == 180 :
                ship[0], ship[1] = -ship[0], -ship[1]
            else :#270°
                ship[0], ship[1] = -ship[1], ship[0]

        else :# "F"
                distance[0] += int(input[i][1:])*ship[0]
                distance[1] += int(input[i][1:])*ship[1]
    print("P2 : Distance : ", abs(distance[0])+abs(distance[1]))         

def find_uber_bus_from_pair(bus_1, bus_2):
    cycle, cycle_start = False, None
    bus_2_relative_delta = bus_2[2] - bus_1[2]
    index = bus_1[0]
    while not cycle:
        bus_2_aligned = (index + bus_2_relative_delta) % bus_2[1] == 0
        if bus_2_aligned:
            if cycle_start is None:
                # start the cycle
                cycle_start = index
            else:
                # cycle found - we've got all we need
                return cycle_start, index - cycle_start, 0
        index += bus_1[1]

def day13(input) :
    earlyTime = int(input[0])
    IDs = list(map(int, input[1].replace(",x", "").split(",")))
    tempID, delay = 0, 1e6
    for id in IDs :
        if 0 < round(earlyTime/id+0.5)*id - earlyTime < delay :
            delay = round(earlyTime/id+0.5)*id - earlyTime
            tempID = id

    print("ID*delay : ", tempID*delay)

    buses = [bus for bus in input[1].split(",")]
    buses_with_deltas = []
    for i, bus in enumerate(buses):
        if bus != "x":
            buses_with_deltas.append((0, int(bus), i))
    current_bus = buses_with_deltas[0]
    for i in range(1, len(buses_with_deltas)):
        current_bus = find_uber_bus_from_pair(current_bus, buses_with_deltas[i])
        
    print("Earliest timestamp : ", current_bus[0])

def day14(input, p) :
    masks = []
    valuesX = []
    mem = [0 for i in range(2**16)]
    j = 0
    ind = 0
    sum_mem_all = 0
    value_bin_temp = ["0" for i in range(36)]
    mem_dict = dict()
    for i in range(len(input)) :
        if "mask" not in input[i] :
            masks[j].append([int(input[i].split("[")[1].split("]")[0]), int(input[i].split(" = ")[1])])
        else :
            if i != 0 :
                j += 1
            masks.append([input[i].split(" = ")[1]])
    for i in range(len(masks)) :
        mask = [masks[i][0][k] for k in range(len(masks[i][0]))]
        for j in range(1, len(masks[i])) :
            mem_i = masks[i][j][0]
            value_bin = "{:036b}".format(masks[i][j][1])
            value_bin = [value_bin[k] for k in range(len(value_bin))]
            if p == 2 :
                bin_mem_i = "{:036b}".format(mem_i)
                value_bin_mem = [bin_mem_i[k] for k in range(len(value_bin))]
            for y in range(len(value_bin)) :
                if mask[y] == "1" :
                    value_bin[y] = "1"
                    if p == 2 :
                        value_bin_mem[y] = "1"
                if mask[y] == "0" :
                    value_bin[y] = "0" 
                if p == 2 and mask[y] == "X" :
                    value_bin_mem[y] = "X"
                    valuesX.append(y)
            if p == 2 :
                bin_tab = []         
                for x in range(2**len(set(valuesX))) :
                    s = "{:0"+str(len(set(valuesX)))+"b}"
                    bin_x = s.format(x)
                    bin_tab.append(bin_x)
                    bin_i = 0
                    for y in range(len(value_bin)) :
                        if value_bin_mem[y] == "X" :
                            value_bin_temp[y] = bin_x[bin_i]
                            bin_i += 1
                        else :
                            value_bin_temp[y] = value_bin_mem[y]
                    mem_i = int("".join(value_bin_temp), 2)
                    mem_dict[str(mem_i)] = masks[i][j][1]
                    mem_i = masks[i][j][0]
                    value_bin_temp = ["0" for z in range(36)]
            valuesX.clear()
    if p == 1 :   
        print("Sum of values left in memory : ", sum(mem))
    if p == 2 :
        for key in mem_dict :
            sum_mem_all += mem_dict[key]        
        print("Sum of values left in memory : ", sum_mem_all)

def day15(input, n) :
    nums = list(map(str, input.split(",")))
    l = len(nums)-1
    i = l
    nb = 0
    while nb < n :
        if nums[i] not in nums[:-1] :
            nums.append("0")
        else :
            if i == l :
                nums.append("0")
            else :
                ind = [index for index, value in enumerate(nums) if value == nums[i]]
                nums.append(str(ind[-1]-ind[-2]))
        nb += 1
        i += 1
    print("30e6th number spoken : ", nums[30e6-1])

    steps, ns = 30000000, [0,3,1,6,7,5]
    last, c = ns[-1], {n: i for i, n in enumerate(ns)}
    for i in range(len(ns) - 1, steps - 1):
        c[last], last = i, i - c.get(last, i)
    print(last)

def day16(input, p) :
    i, j = 0, 0
    ranges = []
    rangesD = []
    while input[i] != "" :
        ranges.append([int(input[i].split(": ")[1].split("-")[0]), int(input[i].split(": ")[1].split("-")[1].split()[0])])
        ranges.append([int(input[i].split("or ")[1].split("-")[0]), int(input[i].split("or ")[1].split("-")[1])])
        if p == 2 :
            rangesD.append([ranges[j], ranges[j+1]])
            j += 2
        i += 1
    ranges = sorted(ranges, key = lambda x:x[0])
    cpt, error, ok = 0, 0, 0
    valids = []
    for j in range(25, len(input))  :
        nums = list(map(int, input[j].split(",")))
        for k in range(len(nums)) :
            for l in range(len(ranges)) :
                if ranges[l][0]<=nums[k]<=ranges[l][1] :
                    cpt += 1
            if cpt == 0 :
                error += nums[k]
                ok += 1
            cpt = 0
        if p == 2 and ok == 0 :
            valids.append(nums)
        ok = 0
    print("Scan error rate : ", error)
    if p == 2 :
        zeros = [0 for k in range(len(rangesD))]
        counts = []
        validsT = list(zip(*valids))
        my_ticket = list(map(int, input[22].split(",")))
        fields = ["" for k in range(len(rangesD))]
        product = 1
        for i in range(len(validsT)) :
            counts.append(zeros)
            for j in range(len(rangesD)) :
                for m in range(len(validsT[i])) :
                    if rangesD[j][0][0]<=validsT[i][m]<=rangesD[j][0][1] or rangesD[j][1][0]<=validsT[i][m]<=rangesD[j][1][1] :
                        counts[i][j] += 1
            zeros = [0 for k in range(len(rangesD))]
        for z in range(len(counts)) :
            tab = [sum(counts[k])/len(counts[k]) for k in range(len(counts))]
            ind = counts[tab.index(min(tab))].index(max(counts[tab.index(min(tab))]))
            fields[tab.index(min(tab))] = input[ind]
            for i in range(len(counts)) :
                counts[i][ind] -= 1
            for i in range(len(rangesD)) :
                counts[tab.index(min(tab))][i] += 1e6
        for i in range(len(fields)) :
            if "departure" in fields[i] :
                product *= my_ticket[i]    
        print("Product of 6 departure fields name : ", product) 
def contestResponse(input) :
    day16(input, 2)
    print("ok")
    
