import sys
data = []

for k in range(18):
    a = len(data)
    b = sys.getsizeof(data)
    data.append(None)
    c = sys.getsizeof(data)
    if c != b:
        print(a)



        
        

