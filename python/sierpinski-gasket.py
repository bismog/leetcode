#!/usr/bin/env python

import sys
import copy

MODEL = 'L '

def get_row_len(matrix):
    max_row = 0
    for m in matrix:
        if m[0] > max_row:
            max_row = m[0]
    return max_row

def get_col_len(matrix):
    max_col = 0
    for m in matrix:
        if m[1] > max_col:
            max_col = m[1]
    return max_col

def display(matrix):
    """
    Print a Signal 'L'(or something like) to where matrix specified.
    """
    xx = get_row_len(matrix)
    yy = get_col_len(matrix)
    # import pdb;pdb.set_trace()
    for x in range(xx+1):
        for y in range(yy+1):
            if [x,y] in matrix:
                print MODEL,
            else:
                print '  ',
        print '\n'

def plus_x(matrix, step):
    # count = len(matrix)
    # import pdb;pdb.set_trace()
    m_copy = copy.deepcopy(matrix)
    for couple in m_copy:
        couple[0] = couple[0] + step
    return m_copy

def plus_y(matrix, step):
    # count = len(matrix)
    # m_copy = matrix[:]
    m_copy = copy.deepcopy(matrix)
    for couple in m_copy:
        couple[1] = couple[1] + step
    return m_copy

def roll(n):
    if n == 0:
        return [[0,0],]
    base_matrix = roll(n-1)
    step = pow(2, n-1)
    plus_x_matrix = plus_x(base_matrix, step)
    plus_x_y_matrix = plus_y(plus_x_matrix, step)
    matrix = base_matrix + plus_x_matrix + plus_x_y_matrix
    return matrix
    

def sierpinski(n):
    """
    """
    m = roll(n)
    # print m
    display(m)

def main():
    if len(sys.argv) != 2:
        print("error imput argument")
        sys.exit(-1)
    sierpinski(int(sys.argv[1]))

if __name__ == "__main__":
    main()

