from my_lib import *
import math 
import hashlib 

nbTests = 26
nbTestReussi = 0

def day_one(input) :
    print("Floor n° : ", count_occurences_in_string(input, "(")-count_occurences_in_string(input, ")"))
    enter = 0
    for i in range(len(input)) :
        if input[i] == "(" :
            enter += 1
        if input[i] == ")" :
            enter -= 1
        if enter == -1 :
            print("Santa first enter : ", i+1)
            break

def day_two(input) :
    feet, slack, bow, wrap = 0, 0, 0, 0
    for i in range(len(input)) :
        eq = input[i].split("x")
        l, w, h = int(eq[0]), int(eq[1]), int(eq[2])
        feet += 2*l*w + 2*w*h + 2*h*l
        slack += min(l*w, w*h, h*l)
        bow += l*w*h
        wrap += 2*min(l, w, h) + 2*second_smallest([l, w, h])
    print("Square feet of wrapping paper : ", feet+slack)
    print("Feet of ribbon : ", bow+wrap)

def day_three(input) :
    coords = [0,0]
    coord_list = ["0,0"]
    for x in input :
        if x == ">":
            coords[0]+=1
        if x == "<": 
            coords[0]-=1
        if x == "^":
            coords[1]+=1
        if x == "v":
            coords[1]-=1
        coord_list.append(str(coords[0])+","+str(coords[1]))
    print ("P1 Houses with at least one present : ", len(set(coord_list)))
    s_coords = [0,0]
    r_coords = [0,0]
    coord_list = ["0,0"]
    i = 0
    for x in input:
        i+=1 
        if x == ">":
            if i % 2 == 0:
                s_coords[0]+=1
            else:
                r_coords[0]+=1
        if x == "<": 
            if i % 2 == 0:
                s_coords[0]-=1
            else:
                r_coords[0]-=1
        if x == "^":
            if i % 2 == 0:
                s_coords[1]+=1
            else:
                r_coords[1]+=1
        if x == "v":
            if i % 2 == 0:
                s_coords[1]-=1
            else:
                r_coords[1]-=1
        if i % 2 == 0:        
            coord_list.append(str(s_coords[0])+","+str(s_coords[1]))
        else:
            coord_list.append(str(r_coords[0])+","+str(r_coords[1]))
        
    print ("P2 Houses with at least one present : ", len(set(coord_list)))


def day_for(str2hash) :
    i = 0
    result = hashlib.md5(str2hash.encode()) 
    while result.hexdigest()[:6] != "000000" :
        string = str2hash[:8] 
        string += str(i)
        result = hashlib.md5(string.encode())
        i += 1
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest()) 
    print("Lowest Positive Number to get 6 zeros : ", i-1)


def day_five(input) :
    vowels = "aeiou"
    letter_prev = ""
    string_not = ("ab", "cd", "pq", "xy")
    not_string, double_letter, three_vowels = False, False, False
    cpt_vowels, cpt_nice, cpt = 0, 0, 0
    for i in range(len(input)) :
        for s in string_not :
            if s not in input[i]:
                cpt += 1
            if cpt == len(string_not) :    
                not_string = True
                break
        for letter in input[i] :
            if letter in vowels :
                cpt_vowels += 1
                if cpt_vowels>=3 :
                    three_vowels = True
            if letter_prev == letter :
                double_letter = True
            letter_prev = letter
        if not_string and double_letter and three_vowels:
            cpt_nice += 1
        not_string, double_letter, three_vowels = False, False, False
        cpt, cpt_vowels = 0, 0
    print("Nice strings : " , cpt_nice)

for numero in range(1, nbTests):
    if str(numero) in ("1", "3", "4") :
        input = open("days/day"+str(numero)+".txt", "r").read()
        #day_one(input)
        if numero == 3 : 
            day_three(input)
        if numero == 4 :
            pass
            #day_for(input)
    if str(numero) in ("2", "5") :
        input = open("days/day"+str(numero)+".txt", "r").read().split("\n")
        if numero == 2 :
            day_two(input[:-1])
        if numero == 5 :
            day_five(input[:-1])

