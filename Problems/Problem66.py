'''
Created on 12.7.2014

@author: Morzeux
'''
import math

def compute_diophantine(x_val, y_val, d_val):
    """ Computes diophantine equation. """
    return x_val**2 - d_val * (y_val**2)

def find_x(dioph_val):
    """ Finds X for Diophantine equation. """
    if math.sqrt(dioph_val) == int(math.sqrt(dioph_val)):
        return None

    m_val = 0
    d_val = 1
    a_val = int(math.sqrt(dioph_val))

    num = a_val
    der = 1

    pom_num = 1
    pom_der = 0

    while compute_diophantine(num, der, dioph_val) != 1:
        m_val = d_val * a_val - m_val
        d_val = int((dioph_val - m_val**2) / d_val)
        a_val = int((int(math.sqrt(dioph_val)) + m_val) / d_val)

        pom_num2 = pom_num
        pom_num = num

        pom_der2 = pom_der
        pom_der = der

        num = a_val * pom_num + pom_num2
        der = a_val * pom_der + pom_der2

    return num

def problem(max_d=1000):
    """
    Consider quadratic Diophantine equations of the form:

        x^2 - D * y^2 = 1

    For example, when D=13, the minimal solution in x is 6492 - 13 * 1802 = 1.

    It can be assumed that there are no solutions in positive integers
    when D is square.

    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
    following:

        3^2 - 2 * 2^2 = 1
        2^2 - 3 * 1^2 = 1
        9^2 - 5 * 4^2 = 1
        5^2 - 6 * 2^2 = 1
        8^2 - 7 * 3^2 = 1

    Hence, by considering minimal solutions in x for D <= 7, the largest x
    is obtained when D=5.

    Find the value of D <= 1000 in minimal solutions of x for which the largest
    value of x is obtained.
    """

    solutions = [(d_value, find_x(d_value)) for d_value in range(2, max_d + 1)]
    solutions = [value for value in solutions if value[1]]
    return sorted(solutions, key=lambda x: x[1])[-1][0]
