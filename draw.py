import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from functools import reduce

# Transfer Function 2 LaTex
def tf2latex(sys):
    # Transfer Function to sympy expression
    s = sp.symbols('s')
    num = sp.Poly(sys.num[0][0], s).as_expr()
    den = sp.Poly(sys.den[0][0], s).as_expr()
    sys_expr = num / den
    # sympy expression to LaTex
    sys_latex = sp.latex(sys_expr)
    return sys_latex

# Draw Step Response
def step_response(sys, T):
    title = f'Step Response of $' + tf2latex(sys) + '$'
    t, y = ctrl.step_response(sys, T)
    plt.plot(t, y)
    plt.title(title, y=1.05)
    plt.xlabel('Time (s)')
    plt.ylabel('Step Response')
    plt.grid()
    plt.show()

# Draw Impulse Response
def impulse_response(sys, T):
    title = f'Impulse Response of $' + tf2latex(sys) + '$'
    t, y = ctrl.impulse_response(sys, T)
    plt.plot(t, y)
    plt.title(title, y=1.05)
    plt.xlabel('Time (s)')
    plt.ylabel('Impulse Response')
    plt.grid()
    plt.show()

# Draw Root Locus
def root_locus(sys):
    title = f'Root Locus of $' + tf2latex(sys) + '$'
    ctrl.root_locus(sys, title='')
    plt.title(title, y=1.05)
    plt.show()

# Draw Bode Plot
def bode_plot(sys):
    title = f'Bode Plot of $' + tf2latex(sys) + '$'
    ctrl.bode_plot(sys, title='')
    plt.title(title, y=1.05)
    plt.show()

# Draw Nyquist Plot
def nyquist_plot(sys):
    title = f'Nyquist Plot of $' + tf2latex(sys) + '$'
    ctrl.nyquist_plot(sys, title='')
    plt.title(title, y=1.05)
    plt.show()


# Define Transfer Function
# K, Numerator and Denominator
K = 1

num = [
    [16]
]

den = [
    [1, 10, 16]
]

num[0] = [K * i for i in num[0]]

# Use functools.reduce to automatically calculate the convolution of multiple polynomials
num_conv = reduce(np.convolve, num)
den_conv = reduce(np.convolve, den)
sys = ctrl.TransferFunction(num_conv, den_conv)

# Draw
step_response(sys, np.linspace(0, 5, 1000))
impulse_response(sys, np.linspace(0, 5, 1000))
root_locus(sys)
bode_plot(sys)
nyquist_plot(sys)






