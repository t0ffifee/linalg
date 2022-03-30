x = [[1,2,3][4,5,6][7,8,9]]
y = [[2,2,2][2,2,2][2,2,2]]

# this can be improved with the operator module
def operation(x, y, operator):
    rows, cols = len(x), len(x[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    for r_i in range(rows):
        for c_i in range(cols):
            if operator == '*':
                el = x[r_i][c_i] * y[r_i][c_i]
            elif operator == '/':
                el = x[r_i][c_i] / y[r_i][c_i]
            elif operator == '+':
                el = x[r_i][c_i] + y[r_i][c_i]
            else:
                el = x[r_i][c_i] - y[r_i][c_i]
            res[r_i][c_i] = el
    return res