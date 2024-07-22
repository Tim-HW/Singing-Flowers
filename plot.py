#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


local = os.path.dirname(os.path.abspath(__file__))


def animate(i):

    data = pd.read_csv(local+'\\csv\\data0.csv')
    r0 = data['Radius']
    y0 = data['Time']

    data = pd.read_csv(local+'\\csv\\data1.csv')
    r1 = data['Radius']
    y1 = data['Time']

    data = pd.read_csv(local+'\\csv\\data2.csv')
    r2 = data['Radius']
    y2 = data['Time']

    plt.cla()

    plt.plot(y0, r0, label='Fleur 1')
    plt.plot(y1, r1, label='Fleur 2')
    plt.plot(y2, r2, label='Fleur 3')
    

    plt.legend(loc='upper left')
    plt.tight_layout()
    time.sleep(1)

while True:
    
    try:
        ani = FuncAnimation(plt.gcf(), animate, interval=1)

        plt.tight_layout()
        plt.show()


    except KeyboardInterrupt:
        break



