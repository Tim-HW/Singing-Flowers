#!/usr/bin/env python3
import pandas as pd
import time
from playsound import playsound
import numpy as np
import os

# 269 a 360
local = os.path.dirname(os.path.abspath(__file__))

# on garde l'ordre avec octave +/-
def play_notes(radius_max):

    do  = local + r'\\notes\\aigue\\do-5aig.mp3'
    re  = local + r'\\notes\\aigue\\re-6aig.mp3'
    mi  = local + r'\\notes\\aigue\\mi-7aig.mp3'
    fa  = local + r'\\notes\\aigue\\fa-1aig.mp3'
    sol = local + r'\\notes\\aigue\\sols-2aig.mp3'
    la  = local + r'\\notes\\aigue\\la-3aig.mp3'
    si  = local + r'\\notes\\aigue\\si-4aig.mp3'


    if radius_max < 280 and radius_max > 270:

        playsound(la)
        return('La')

    elif radius_max < 270 and radius_max > 260:

        playsound(sol)
        return("sol")

    elif radius_max < 260 and radius_max > 250:
        
        playsound(fa)
        return("fa")

    elif radius_max < 250 and radius_max > 240:
        playsound(mi)
        return("mi")

    elif radius_max < 240 and radius_max > 230:
        playsound(re)
        return("Re")
    
    elif radius_max < 230 and radius_max > 220:
        playsound(do)
        return("Do")
    
    elif radius_max < 220 and radius_max > 210:
        playsound(si)
        return("Si")

    elif radius_max < 210 and radius_max > 200:
        playsound(la)
        return("La")

    elif radius_max < 200 and radius_max > 190:
        playsound(sol)
        return("Sol")

    elif radius_max < 190 and radius_max > 180:
        playsound(fa)
        return("fa")
    else:
        pass



if __name__ == "__main__":
    
    time.sleep(3)

    while True:

        try:
            
            data = pd.read_csv(local +r'\\csv\\data2.csv')
            r = data['Radius']
            
            if len(r) != 0 :

                radius = r[len(r)-1]
                timer = np.random.normal(3, 1, 1)
                
                print(play_notes(radius))
                

                time.sleep(abs(timer[0]))


        except KeyboardInterrupt:
            break

