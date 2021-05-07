import numpy as np


def punto_fijo(g, p0, TOL, N0):
    i = 1

    while i <= N0:
        p = g(p0)

        if np.abs(p - p0) < TOL:
            return p, i

        i = i + 1
        p0 = p

    print("no converge")
    return p0, -1

def punto_fijo_historial(g, p0, TOL, N0):
    historial = []
    i = 1

    while i <= N0:
        
        p = g(p0)
        historial.append((i, p))
        
        if np.abs(p - p0) < TOL:
            return p, i, historial

        i = i + 1
        p0 = p

    print("no converge")
    return p0, -1, historial

def g(x):
    return (1/2) * (10  - x ** 3) ** (1/2)

# parametros para testear

p0 = 1.5
tol = 1e-5
max_iter = 30

raiz, iteraciones = punto_fijo(g, p0, tol, max_iter)

print("la raiz es: ", raiz, "encontrada en ", iteraciones, " iteracioes.")


raiz, iteraciones, historial = punto_fijo_historial(g, p0, tol, max_iter)
for i in historial:
    print("la raiz es: ", i[1], "encontrada en ", i[0], " iteracioes.")


