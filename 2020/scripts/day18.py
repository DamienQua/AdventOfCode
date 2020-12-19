import re

def find_brackets(line) :
    open = [index for index, value in enumerate(line) if value == "("]
    close = [index for index, value in enumerate(line) if value == ")"]
    brackets = []
    while len(open)>0 :
        if len(open) == 1 :
            brackets.append([open[0], close[0]])
            open.pop(0); close.pop(0)
        for j in range(1, len(open)) :
            if close[j-1] > open [j-1] and close[j-1] < open [j] :
                brackets.append([open[0], close[j-1]])
                open.pop(0); close.pop(j-1)
                break
    return brackets

def find_product(line) :
    return [index for index, value in enumerate(line) if value == "*"]

def find_sum(line) :
    return [index for index, value in enumerate(line) if value == "+"]

def evaluate_expression(line) :
    in_brackets = False
    not_in = []
    brackets = find_brackets(line)
    for i in range(len(line)) :
        for j in range(len(brackets)) :
            if brackets[j][0]<=i<=brackets[j][1] :
                in_brackets = True
                break
        if in_brackets == False :
            not_in.append(i)
        in_brackets = False
    for i in range(len(line)) :
        if i not in not_in :
            pass


def sum_results(input) :
    s = 0
    for line in input :
        #lines = re.findall(r"[\w\(-]+[\w\)-]", line)
        s += eval(line.replace(" ", ""))
        #evaluate_expression(line.replace(" ", ""))
    print(s)

input = open("inputs/day18.txt", "r").read().split("\n")[:-1]
sum_results(input)
