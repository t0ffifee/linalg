from random import randint

# this can be improved with the operator module
def operation(a, b, operator):
    rows, cols = len(a), len(a[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    for r_i in range(rows):
        for c_i in range(cols):
            if operator == '*':
                el = a[r_i][c_i] * b[r_i][c_i]
            elif operator == '/':
                el = a[r_i][c_i] / b[r_i][c_i]
            elif operator == '+':
                el = a[r_i][c_i] + b[r_i][c_i]
            else:
                el = a[r_i][c_i] - b[r_i][c_i]
            res[r_i][c_i] = el
    return res

def dot(a, b):
    rows_a, cols_b = len(a), len(b[0])
    if rows_a != cols_b:
        print('impossible combination')
        return
    res = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    r, c = 0, 0
    for r in range(rows_a):
        for c in range(cols_b):
            row, col = a[r], [el[c] for el in b]
            el = sum(el_r*el_c for el_r,el_c in zip(row, col))
            res[r][c] = el  
    return res

def inner_product(a, b):
    products = [x*y for x,y in zip(a,b)]
    return sum(products)

def print_matrix(m):
    for r in m:
        for c in r:
            print(c, end=' ')
        print()

def rand_matrix(x, y):
    matrix = [[randint(1,9) for _ in range(x)] for _ in range(y)]
    return matrix

