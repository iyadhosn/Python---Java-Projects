import math as m
import sys

j = 0
def listToDict(List):
    newKey = {}
    for i in range(0, len(List), 2):
        newKey[List[i]] = List[i + 1]
    return newKey


def straightLineDistance(x1, y1, x2, y2):
    x1 = m.radians(x1)
    x2 = m.radians(x2)
    y1 = m.radians(y1)
    y2 = m.radians(y2)
    d = 2 * 3958.8 * m.asin(m.sqrt((m.sin((y1 - x1) / 2)) ** 2 + m.cos(x1) * m.cos(y1) * (m.sin((y2 - x2) / 2) ** 2)))
    return d


def aStar(current, goal):
    notvisited.clear()
    global j
    for i in mapDict.get(current):
        h = float(heuristic.get(i))
        g = float(mapDict.get(current).get(i)) + float(visited[j][2])
        notvisited.append((i, g + h, g))
    visited.append(min(notvisited, key=lambda x: x[1]))
    notvisited.remove(min(notvisited, key=lambda x: x[1]))
    for i in notvisited:
        if i[0] == goal:
            x.append((i[0], float(i[1])))

    if visited[-1][0] == goal and len(x) == 1:
        if x[0][1] < visited[-1][1]:
            visited.pop()
            visited.pop()
            visited.append(x[0])
            print("From city: ", startLocation)
            print("To city: ", endLocation)
            for i in range(len(visited)):
                print(visited[i][0], end="-")
            print("Total distance: ", format(visited[-1][1], ".2f"))

    elif visited[-1][0] == goal:
        print("From city: ", startLocation)
        print("To city: ", endLocation)
        for i in range(len(visited)):
            print(visited[i][0], end="-")
        print("Total distance: ", format(visited[-1][1], ".2f"))

    else:
        j += 1
        aStar(visited[-1][0], goal)


if __name__ == '__main__':
    x = []
    visited = []
    notvisited = []
    #startLocation = sys.argv[1]
    #endLocation = sys.argv[2]
    startLocation = input()
    endLocation = input()

    visited.append((startLocation, 0, 0))
    # SETTING UP CORD.TXT
    # -------------------
    f = open('coordinates.txt', 'r')
    contents = f.readlines()
    cordDict = {}
    for i in contents:
        cordDict[(i.split(':')[0])] = i.split(':')[1].replace("(", "").replace(")", "").split(",")
    heuristic = {}
    for k, v in cordDict.items():
        heuristic[k] = straightLineDistance(float(v[0]), float(cordDict.get(endLocation)[0]), float(v[1]), float(cordDict.get(endLocation)[1]))
    f.close()

    # print(heuristic.items())
    # -------------------
    # SETTING UP MAP.TXT
    # -------------------
    f = open('map.txt', 'r')
    mapDict = {}
    contents = f.readlines()
    for i in contents:
        mapDict[i.split('-')[0]] = i.split('-')[1].replace("(", " ").replace(")", "").replace(" ", ",").split(',')
    for k, v in mapDict.items():
        v = listToDict(v)
        mapDict[k] = v
    f.close()
    aStar(startLocation, endLocation)
