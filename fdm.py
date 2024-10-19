import numpy as np

N = 50

def solve_heat_equation(params):
    paramsdict ={}
    for param in params:
        paramsdict[param] =float(params[param])

    k = paramsdict["k"]
    q = paramsdict["q"]
    L = paramsdict["L"]
    Ttop = paramsdict["Ttop"]
    Tbtm = paramsdict["Tbtm"]
    Tleft = paramsdict["Tleft"]
    Tright = paramsdict["Tright"]

    x = np.linspace(0,L,N)
    y = np.copy(x)

    dx = x[1] - x[0]
    dy = dx

    A = np.zeros((N*N,N*N))
    B = np.zeros(N*N)

    for i in range(N*N):
        if i % N == 0:
            A[i,i] = 1
            B[i] = Tleft
        elif (i-N+1) % N == 0:
            A[i,i] = 1
            B[i] = Tright
        elif (i < N):
            A[i,i] = 1
            B[i] = Tbtm
        elif (i >= N*(N-1)):
            A[i,i] = 1
            B[i] = Ttop
        else:
            A[i,i] = -2/dx**2 - 2/dy**2 # Central node
            
            A[i,i-1] = 1/dx**2 # Left node 
            A[i,i+1] = 1/dx**2 # Right node

            A[i,i+N] = 1/dy**2 # Upper node
            A[i,i-N] = 1/dy**2 # Lower node

            B[i] =  -q/k # Source term
    
    sol = np.linalg.solve(A,B).reshape(N,N)

    return x.tolist(),y.tolist(),sol.tolist()

