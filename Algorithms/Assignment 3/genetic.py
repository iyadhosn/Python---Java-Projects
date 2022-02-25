from board import Board
import random
import datetime


def buildString(state):
    string = ""
    for i in state:
        for j in i:
            if j == 1:
                string += str(i.index(1) + 1)
    return string


def selection(string1, string2, string3, string4, string5, string6, string7, string8):
    state1Fitness = 10 - state1.get_fitness()
    state2Fitness = 10 - state2.get_fitness()
    state3Fitness = 10 - state3.get_fitness()
    state4Fitness = 10 - state4.get_fitness()
    state5Fitness = 10 - state5.get_fitness()
    state6Fitness = 10 - state6.get_fitness()
    state7Fitness = 10 - state7.get_fitness()
    state8Fitness = 10 - state8.get_fitness()

    state1chance = state1Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state2chance = state2Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state3chance = state3Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state4chance = state4Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state5chance = state5Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state6chance = state6Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state7chance = state7Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)
    state8chance = state8Fitness / (state1Fitness + state2Fitness + state3Fitness + state4Fitness + state5Fitness + state6Fitness + state7Fitness + state8Fitness)

    r = random.uniform(0, 1)
    if r < state1chance:
        return string1
    elif r < state1chance + state2chance:
        return string2
    elif r < state1chance + state2chance + state3chance:
        return string3
    elif r < state1chance + state2chance + state3chance + state4chance:
        return string4
    elif r < state1chance + state2chance + state3chance + state4chance + state5chance:
        return string5
    elif r < state1chance + state2chance + state3chance + state4chance + state5chance +state6chance:
        return string6
    elif r < state1chance + state2chance + state3chance + state4chance + state5chance + state6chance + state7chance:
        return string7
    else:
        return string8


def crossover(s1, s2, s3, s4, s5, s6, s7, s8):
    splitpoint12 = random.randrange(1, 5)
    splitpoint34 = random.randrange(1, 5)
    splitpoint56 = random.randrange(1, 5)
    splitpoint78 = random.randrange(1, 5)

    string1 = ""
    string2 = ""
    string1 += s1[:splitpoint12] + s2[splitpoint12:]
    string2 += s2[:splitpoint12] + s1[splitpoint12:]

    string3 = ""
    string4 = ""
    string3 += s3[:splitpoint34] + s4[splitpoint34:]
    string4 += s4[:splitpoint34] + s3[splitpoint34:]


    string5 = ""
    string6 = ""
    string5 += s5[:splitpoint56] + s6[splitpoint56:]
    string6 += s6[:splitpoint56] + s5[splitpoint56:]

    string7 = ""
    string8 = ""
    string7 += s7[:splitpoint78] + s8[splitpoint78:]
    string8 += s8[:splitpoint78] + s7[splitpoint78:]

    return string1, string2, string3, string4, string5, string6, string7, string8


def mutation(s):
    r = random.randrange(0, 5)
    index = random.randrange(1, 5)
    if r == 0:
        return s
    else:
        return s[0:index] + str(r) + s[index + 1:]

def stringto2dArray(s):
    state = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
            ]
    count = 0
    for i in s:
        state[count][int(i) - 1] = 1
        count += 1

    return state


def GA(s1, s2, s3, s4, s5, s6, s7, s8):
    if 10 - s1.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s1.show_map()
    elif 10 - s2.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s2.show_map()
    elif 10 - s3.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s3.show_map()
    elif 10 - s4.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s4.show_map()
    elif 10 - s5.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s5.show_map()
    elif 10 - s6.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s6.show_map()
    elif 10 - s7.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s7.show_map()
    elif 10 - s8.get_fitness() == 10:
        endTime = datetime.datetime.now()
        runTime = endTime - startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        s8.show_map()
    else:

        string1 = buildString(Board(5).map)
        string2 = buildString(Board(5).map)
        string3 = buildString(Board(5).map)
        string4 = buildString(Board(5).map)
        string5 = buildString(Board(5).map)
        string6 = buildString(Board(5).map)
        string7 = buildString(Board(5).map)
        string8 = buildString(Board(5).map)

        selectedString1 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString2 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString3 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString4 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString5 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString6 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString7 = selection(string1, string2, string3, string4, string5, string6, string7, string8)
        selectedString8 = selection(string1, string2, string3, string4, string5, string6, string7, string8)

        crossedstrings = crossover(selectedString1, selectedString2, selectedString3, selectedString4, selectedString5, selectedString6, selectedString7, selectedString8)
        string1 = crossedstrings[0]
        string2 = crossedstrings[1]
        string3 = crossedstrings[2]
        string4 = crossedstrings[3]
        string5 = crossedstrings[4]
        string6 = crossedstrings[5]
        string7 = crossedstrings[6]
        string8 = crossedstrings[7]

        string1 = mutation(string1)
        string2 = mutation(string2)
        string3 = mutation(string3)
        string4 = mutation(string4)
        string5 = mutation(string5)
        string6 = mutation(string6)
        string7 = mutation(string7)
        string8 = mutation(string8)

        state1.map = stringto2dArray(string1)
        state2.map = stringto2dArray(string2)
        state3.map = stringto2dArray(string3)
        state4.map = stringto2dArray(string4)
        state5.map = stringto2dArray(string5)
        state6.map = stringto2dArray(string6)
        state7.map = stringto2dArray(string7)
        state8.map = stringto2dArray(string8)
        GA(state1, state2, state3, state4, state5, state6, state7, state8)


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    state1 = Board(5)
    state2 = Board(5)
    state3 = Board(5)
    state4 = Board(5)
    state5 = Board(5)
    state6 = Board(5)
    state7 = Board(5)
    state8 = Board(5)
    GA(state1, state2, state3, state4, state5, state6, state7, state8)






