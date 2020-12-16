from main import contestResponse

nbTests = 17
nbTestReussi = 0

for numero in range(16, nbTests):
    input = open("tests/input"+str(numero)+".txt", "r").read().split("\n")
    result = contestResponse(input[:-1])
