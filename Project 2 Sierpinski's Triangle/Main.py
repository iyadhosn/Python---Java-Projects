#Iyad Aboul Hosn
import turtle

def Sierpinski(turtle, order, direction):
    if order == 0:
        turtle.forward(direction)
        Cords.append(t.pos())
    else:
        fractal(turtle, order - 1, direction)
        turtle.left(60)
        Sierpinski(turtle, order - 1, direction)
        turtle.left(60)
        fractal(turtle, order - 1, direction)

def fractal(turtle, order, direction):
    if order == 0:
        turtle.forward(direction)
        Cords.append(t.pos())
    else:
        Sierpinski(turtle, order - 1, direction)
        turtle.right(60)
        fractal(turtle, order - 1, direction)
        turtle.right(60)
        Sierpinski(turtle, order - 1, direction)

def peepeepoopoo(a, b, c, d, e, f ):
    num = (float(d - b) * (e - c)) - float((c - a) * (f - d))
    if num == 0:
        return 0
    elif num > 0:
        return 1
    return 2

def LESALAM(a, b, c, d, e, f):
    w = max(a, e)
    x = min(a, e)
    y = max(b, f)
    z = min(b, f)

    if((c <= w) and (c >= x) and (d <= y) and (d >= z)):
        return True
    return False

def intersection(line1, line2):
    LOnex1 = line1[0]
    LOney1 = line1[1]
    LTwox1 = line2[0][0]
    LTwoy1 = line2[0][1]
    LOnex2 = line1[2]
    LOney2 = line1[3]
    LTwox2 = line2[1][0]
    LTwoy2 = line2[1][1]
    pathing1 = peepeepoopoo(LOnex1, LOney1, LOnex2, LOney2, LTwox1, LTwoy1)
    pathing2 = peepeepoopoo(LOnex1, LOney1, LOnex2, LOney2, LTwox2, LTwoy2)
    pathing3 = peepeepoopoo(LTwox1, LTwoy1, LTwox2, LTwoy2, LOnex1, LOney1)
    pathing4 = peepeepoopoo(LTwox1, LTwoy1, LTwox2, LTwoy2, LOnex2, LOney2)
    portion1 = LESALAM(LOnex1, LOney1, LTwox1, LTwoy1, LOnex2, LOney2)
    portion2 = LESALAM(LOnex1, LOney1, LTwox2, LTwoy2, LOnex2, LOney2)
    portion3 = LESALAM(LTwox1, LTwoy1, LOnex1, LOney1, LTwox2, LTwoy2)
    portion4 = LESALAM(LTwox1, LTwoy1, LOnex2, LTwoy2, LTwox2, LTwoy2)
    if(((pathing1 != pathing2) and (pathing3 != pathing4)) or (portion1 and (pathing1 == 0)) or (portion2 and (pathing2 == 0)) or (portion3 and (pathing3 == 0)) or (portion4 and (pathing4 == 0))):
        Solution.append(1)
        return 1
    Solution.append(0)
    return 0

def Organization(toBeOrganized, splitPoint):
    OrganizedSolution = []
    for i in range(0, len(toBeOrganized) , splitPoint):
        yield toBeOrganized[i:i+splitPoint]
    return OrganizedSolution

if __name__=="__main__":
    t = turtle.Turtle()
    turtle.speed(100)
    Cords = []
    File = input('Input file name: ')
    File = open(File, 'r')
    #File = open("input.txt", 'r')
    number = File.readlines()
    input = []
    for i in number:
        input.append(i)
    n = input[0]
    input.remove(n)
    test = []
    for i in input:
        z = 0
        for j in range(len(i)):
            if j == len(i) - 1:
                test.append(float(i[z:]))
                break
            if i[j] == " ":
                test.append(float(i[z:j]))
                z = j + 1
    input = test
    test1 = []
    v = 0
    w = 1
    x = 2
    y = 3
    while y <= len(input):
        test1.append((input[v], input[w], input[x], input[y]))
        v += 4
        w += 4
        x += 4
        y += 4
    input = test1
    if (int(n) % 2 != 0):
       t.setheading(60)
    Cords.append(t.pos())
    fractal(t, int(n), 7)
    Solution = []
    for i in range(len(input)):
        for j in range(len(Cords) - 1):
            intersection(input[i], (Cords[j], Cords[j+1]))
    Output = []
    split = len(Cords) - 1
    x = list(Organization(Solution, split))
    for i in x:
        if 1 in i:
            Output.append(int(1))
        else:
            Output.append(int(0))
    f = open("output.txt", "w")
    for c in Output:
        f.write(str(c))
        f.write("\n")
    f.close()
    quit()
    turtle.done()