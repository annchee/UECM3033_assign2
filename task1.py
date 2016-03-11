# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:21:13 2016

@author: Admin
"""

import numpy as np
#Your optional code here
#You can import some modules or create additional functions
import scipy.linalg as lp
ITERATION_LIMIT =50
def lu(A, b):
    #sol = []
    # Edit here to implement your code
    L,U=lp.lu(A,True)
    y=lp.solve(L,b)
    x=lp.solve(U,y)
   
    return list(x)

def sor(A, b):
    #sol = []
    # Edit here to implement your code
    n=len(A)
    # A=D-L-U
    # solve D
    D=np.zeros_like(A)
    for i in range(n):
        D[i][i]=A[i][i]
     # solve L
    L=np.zeros_like(A)
    for i in range (n):
        for j in range(i):
            L[i][j]=-A[i][j]
     # solve U
    U=np.zeros_like(A)
    for i in range (n):
        for j in range(i+1,n):
            U[i][j]=-A[i][j]
    
    #omega
    K=np.zeros_like(A)
    for i in range (n):
        K[i][j]=1/D[i][j]
    eig=lp.eigvals(K)
    p=max(abs(eig))
    omega=2*(1-np.sqrt(1-np.power(p,2)))/np.power(p,2)
    if (omega<=0.0 or omega>=2.0):
        omega=1.03
    Q = D/omega -L
    K = np.linalg.inv(Q).dot(Q-A)
    c = np.linalg.inv(Q).dot(b)
    x = np.zeros_like(b)
    for iteration in range (ITERATION_LIMIT):
        x= K.dot(x)+c
    return list(x)

def solve(A, b):
    condition = Check(A) # State and implement your condition here
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b)
#condition
def Check(A):
    try:
        #Check strictly diagonal dominant
        temp=2*np.diag(A)>np.sum(np.abs(A),1)
        result=temp.all()
        if (result):
            #solve by LU
            return True
    
        #Check possitive Definite Matrix
        np.linalg.cholesky(A)
    except np.linalg.linalg.LinAlgError:
        #solve by lu
        return True
    return False

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]
    sol = solve(A,b)
    print(sol)
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    sol = solve(A,b)
    print(sol)