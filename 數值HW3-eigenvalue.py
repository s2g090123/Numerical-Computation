import numpy as np
import math
A = np.array([[4,3,0.05],[3,4,-1],[0.05,-1,4]])
b = np.array([[24],[30],[-24]])
number = 0
m = len(A)     # the matrix size
L = np.tril(A,-1) 
U = np.triu(A,1)
D = np.zeros([m,m]) 
x1 = np.ones([m,1])
for i in range(m):
    D[i,i] = A[i,i]

T_j = np.dot(np.linalg.inv(D),np.add(L,U))
E = np.linalg.eigvals(T_j)
maxE = np.amax(E)
omega = 1.5  # the ω value
omega2 = 2/(1+math.sqrt((1-pow(maxE,2)))) # the best choose ω value

x2 = np.dot(np.dot(np.linalg.inv(D+omega*L),((1-omega)*D-omega*U)),x1)+omega*np.dot(np.linalg.inv(D+omega*L),b)
while(np.linalg.norm(x1-x2)>0.0000001):   # 7 decimal
    x1 = x2
    x2 = np.dot(np.dot(np.linalg.inv(D+omega*L),((1-omega)*D-omega*U)),x1)+omega*np.dot(np.linalg.inv(D+omega*L),b)
    number+=1
print('the omega is ',omega)
print (number)
print (x1)

number = 0
x1 = np.ones([m,1])
x2 = np.dot(np.dot(np.linalg.inv(D+omega2*L),((1-omega2)*D-omega2*U)),x1)+omega2*np.dot(np.linalg.inv(D+omega2*L),b)
while(np.linalg.norm(x1-x2)>0.0000001):   # 7 decimal
    x1 = x2
    x2 = np.dot(np.dot(np.linalg.inv(D+omega2*L),((1-omega2)*D-omega2*U)),x1)+omega2*np.dot(np.linalg.inv(D+omega2*L),b)
    number+=1
print('the omega is ',omega2)
print (number)
print (x1)