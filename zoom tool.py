import numpy as np

b = 0.5
s = 0.125

arr = np.array([[ (b+s,b+s) ,0.1 ,0.2 ,0.3 ,0.4 ],
                [1.0,1.1 ,1.2 ,1.3 ,1.4 ],
                [2.0,2.1 ,2.2 ,2.3 ,2.4 ]])



print(arr)

print(arr[0,0])
print(type(arr[0,0]))
