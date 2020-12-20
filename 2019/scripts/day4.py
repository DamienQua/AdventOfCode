# https://adventofcode.com/2019/day/4
#--- Day 4: Secure Container ---

a, b = 240298, 784956

def isValid (password) :
    doubles = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    dbl, up = False, True
    for i in range(len(doubles)) :
        if str(doubles[i]) in password :
            dbl = True
            break
    if dbl == True :
        for i in range(1, len(password)):
            if password[i]<password[i-1] :
                up = False 
                break
    return 1 if up == True and dbl == True and len(password) == 6 else 0 

# Part 1 :
good_pwd = [isValid (str(pwd)) for pwd in range(a, b+1)]
print("Passwords that meet these criteria : ", sum(good_pwd))

# Part 2 :
nbPassword = 0
for pwd in range(a, b+1) :
    for number in str(pwd) :
        if str(pwd).count(number) == 2 and good_pwd[pwd-a] == 1 :
            nbPassword += 1           
            break 
print("Passwords that meet these criteria : ", nbPassword)
