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