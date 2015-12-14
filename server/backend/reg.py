__author__ = 'Jian Yang'
__date__ = '12/13/15'

import numpy as np
import matplotlib.pyplot as plt

def get_regression(x, y):
    fit, residuals, rank, singular_values, rcond = np.polyfit(x,y,1, full = True)
    fit_fn = np.poly1d(fit)

    p1_x = min(x)
    p2_x = max(x)
    return (p1_x, fit_fn(p1_x)), (p2_x, fit_fn(p2_x)), residuals

if __name__ == '__main__':
    x = np.array([1,2,3,4])
    y = np.array([3,5,7,10]) # 10, not 9, so the fit isn't perfect
    p1, p2, error = get_regression(x, y)
    plt.plot(x, y, 'yo')
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
    plt.xlim(0, 5)
    plt.ylim(0, 15)
    plt.show()

    # plt.plot(x,y, 'yo', x, fit_fn(x), '--k')