# Iyad Aboul Hosn
import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def extended(c, d):
    if c != 0:
        factor, x, y = extended(d % c, c)
        num = d/c
        num = math.trunc(num)
        j = (y - num * x)
        return (factor, j, x)
    else:
        return (d, False, True)

def euc(one, two, three, n):
    w = gcd(one, two)
    one = one//w
    two = two//w
    factor, x, y = extended(w, three)
    if n % factor != 0:
        return 0, 0, 0, 0
    factor *= n
    x *= n
    y *= n
    factor1, x1, y1 = extended(one, two)
    x1 *= x
    y1 *= x
    one *= w
    two *= w
    goal = (one * x1) + (two * y1) + (three * y)
    if goal == n:
        return True, x1, y1, y
    return 0

if __name__=="__main__":

    #File = input('Input file name: ')
    #File = open(File, 'r')
    File = open("input.txt", 'r')
    numbers = File.readlines()
    Ms = []
    for i in numbers:
        Ms.append(int(i))
    x = Ms[0]
    Ms.remove(x)
    i = 0
    j = 1
    k = 2
    while True:
        solution = euc(Ms[i], Ms[j], Ms[k], x)
        if solution[0] != 0:
            f = open("output.txt", "w")
            lines = [(Ms[i], solution[1]), (Ms[j], solution[2]), (Ms[k], solution[3])]
            for c in lines:
                f.write(str(c[0]))
                f.write(" ")
                f.write(str(c[1]))
                f.write("\n")
            f.close()
            quit()
        elif k + 1 == len(Ms) and j + 1 == len(Ms) - 1:
            i += 1
            j = i + 1
            k = j + 1
        elif k + 1 == len(Ms):
            j += 1
            k = j + 1
        else:
            k += 1






