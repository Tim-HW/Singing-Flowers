#!/usr/bin/env python3
import pandas as pd
import time
from playsound import playsound
import numpy as np
import os

# 269 a 360
local = os.path.dirname(os.path.abspath(__file__))

# 269 a 360

def play_notes(radius_max):

    do  = local + r'\\notes\\do-5.mp3'
    re  = local + r'\\notes\\re-6.mp3'
    mi  = local + r'\\notes\\mi-7.mp3'
    fa  = local + r'\\notes\\fa-1.mp3'
    sol = local + r'\\notes\\sols-2.mp3'
    la  = local + r'\\notes\\la-3.mp3'
    si  = local + r'\\notes\\si-4.mp3'


    if radius_max > 360:
        playsound(si)
        return("Si")


    elif radius_max < 350 and radius_max > 340:
        playsound(la)
        return("La")


    elif radius_max < 340 and radius_max > 330:
        playsound(sol)
        return("Sol")      

    elif radius_max < 330 and radius_max > 320:
        playsound(fa)
        return("fa")

    elif radius_max < 320 and radius_max > 310:
        playsound(re)
        return("re")
    
    elif radius_max < 310 and radius_max > 300:
        playsound(do)
        return("do")
    
    elif radius_max < 300 and radius_max > 180:
        playsound(si)
        return('si')

    elif radius_max < 180 and radius_max > 170:
        playsound(la)
        return("La")

    elif radius_max < 170 and radius_max > 160:
        playsound(sol)
        return("Sol")

    elif radius_max > 150:
        playsound(fa)
        return("fa")




if __name__ == "__main__":

    time.sleep(2)
   
    while True:

        try:
            
            data = pd.read_csv(local +r'\\csv\\data1.csv')
            r = data['Radius']
            
            if len(r) != 0 :

                radius = r[len(r)-1]
                timer = np.random.normal(3, 1, 1)
        
                print("note jouer par la fleur 2 :", play_notes(radius))
                

                time.sleep(abs(timer[0]))


        except KeyboardInterrupt:
            break

