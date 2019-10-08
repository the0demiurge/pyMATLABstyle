# MATLAB style numpy and sympy

Create matrix, call function in MATLAB style

## Installation

`pip install pyMATLABstyle`

## Import

```python
from MATLAB import *
```

## MATLAB style numpy
Includes:
1. mat
2. inv
3. rank
4. det
5. exp


```python
matN = mat('1 2 3;4 7,2;6,7,8')
print('matN:', matN, sep='\n')
```

    matN:
    [[1 2 3]
     [4 7 2]
     [6 7 8]]



```python
print('rank:', rank(matN))
print('inv:', inv(matN) * (matN), sep='\n')
print('det:', det(matN))
print('exp:', exp(matN, 2) - matN * matN, sep='\n')
```

    rank: 3
    inv:
    [[ 1.00000000e+00  2.77555756e-16  4.44089210e-16]
     [ 3.33066907e-16  1.00000000e+00  0.00000000e+00]
     [-3.46944695e-17 -5.89805982e-17  1.00000000e+00]]
    det: -40.000000000000014
    exp:
    [[0 0 0]
     [0 0 0]
     [0 0 0]]


## MATLAB style syms
syms == sympy.symbols


```python
x, y, z = syms('x, y z')
f = x**(y - z)
print(f)
```

    x**(y - z)


## MATLAB style sympy matrix
Includes:
1. smat
2. sinv
3. sdet
4. sexp


```python
matS = smat('x11 x12 x13;x21,x22,x23;x31,x32 x33')
print('matS:', matS, sep='\n')

```

    matS:
    Matrix([[x11, x12, x13], [x21, x22, x23], [x31, x32, x33]])



```python
print('rank:', matS.rank())
print('inv:', sinv(matS) * (matS), sep='\n')
print('det:', sdet(matS))
print('exp:', sexp(matS, 2) - matS * matS, sep='\n')
```

    rank: 3
    inv:
    Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    det: x11*x22*x33 - x11*x23*x32 - x12*x21*x33 + x12*x23*x31 + x13*x21*x32 - x13*x22*x31
    exp:
    Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

