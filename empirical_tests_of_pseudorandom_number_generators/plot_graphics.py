import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_density(otr_s_tal, c, exp_func,x_min, x_max, x_delta):
    fig, ax = plt.subplots()
    ax.hist(otr_s_tal, len(c), density=True, color='g')
    ax.plot(np.arange(x_min, x_max, x_delta), exp_func, color='r')
    plt.show()
