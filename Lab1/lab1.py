import numpy as np
a = [[1,1],[1,-1]]
b = [0,2]
x = np.linalg.solve(a,b)
print(x)
for i in range(4):
    print(i)