#!/usr/bin/env python3

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import time


def output(frame0,frame1,frame2):

    try: 
        taille = 0.7

        frame0 = cv2.resize(frame0,(0,0),None,taille,taille)
        frame1 = cv2.resize(frame1,(0,0),None,taille,taille)
        frame2 = cv2.resize(frame2,(0,0),None,taille,taille)

        final_frame = np.hstack((frame0,frame1,frame2))  
        cv2.imshow('frame',final_frame)  
    except:
        pass 





def ellipse(img,frame):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the rotated rectangles and ellipses for each contour

    liste       = list()
    minEllipse  = [None]*len(contours)

    for i, c in enumerate(contours):
        
        if c.shape[0] > 5:
            
            minEllipse[i] = cv2.fitEllipse(c)
            

    for i in range(len(minEllipse)):
      
        if minEllipse[i] != None:

            liste.append(minEllipse[i][1][0])

        else:

            liste.append(0)


    k = liste.index(max(liste))

    if minEllipse[k] != None:
    
        #print(minEllipse[k][1][1])
        color = (0,0,200)
        # ellipse
        cv2.ellipse(frame, minEllipse[k], color, 2)


    return frame,max(liste)






def write_cvs(data,nbr):




    fieldnames = ["Radius", "Time"]

    with open(local + '\\csv\\data'+str(nbr)+'.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        now = datetime.now()
        current_time = time.time() - timer


        info = {
            "Radius": data,
            "Time"  : current_time,
        }

        csv_writer.writerow(info)
       






if __name__ == "__main__":

    local = os.path.dirname(os.path.abspath(__file__))

    timer = time.time()
    
    treshold = 1

    fieldnames = ["Radius", "Time"]
    
    for nbr in range(3):

        with open(local +'\\csv\\data'+str(nbr)+'.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()



    list0 = list()
    list1 = list()
    list2 = list()

    # Open Video file
    cap0 = cv2.VideoCapture(local+r'\\video\\rose1def_acc.mp4')
    cap1 = cv2.VideoCapture(local+r'\\video\\rose2def_acc.mp4') 
    cap2 = cv2.VideoCapture(local+r'\\video\\rose3def_acc.mp4')

    # cap0.isOpened() or cap1.isOpened() or cap2.isOpened()
    # Loop that plays every frame of the video until the end


    while(1): 


        try:
            
            # loop cette merde pour de vrai STP

            # Retrive frame and success of the reading
            lower_Blue = np.array([0,0,0])
            upper_Blue = np.array([130,130,244])

            if cap0.isOpened():

                try:
                    ret0, frame0 = cap0.read() 

                    if ret0 == False :
                        cap0 = cv2.VideoCapture(local+r'\\video\\rose1def_acc.mp4')

                    ret0, frame0 = cap0.read() 
                    mask0 = cv2.inRange(frame0, lower_Blue, upper_Blue) 
                    res0 = cv2.bitwise_and(frame0,frame0, mask= mask0)
                    img0 = cv2.GaussianBlur(mask0,(9,9),10)
                    frame0,eli0 = ellipse(img0,frame0)

                    
                except:
                    pass

            

            

            if cap1.isOpened():

                try:
                    ret1, frame1 = cap1.read()    
                    
                    if ret1 == False :
                        cap1 = cv2.VideoCapture(local+r'\\video\\rose2def_acc.mp4')

                    ret1, frame1 = cap1.read()   
                    mask1 = cv2.inRange(frame1, lower_Blue, upper_Blue) 
                    res1 = cv2.bitwise_and(frame1,frame1, mask= mask1)
                    img1 = cv2.GaussianBlur(mask1,(9,9),10)
                    frame1,eli1 = ellipse(img1,frame1)


                except:

                    pass

            if cap2.isOpened():

                try:
                
                    ret2, frame2 = cap2.read()     
                    
                    if ret2 == False :
                        cap2 = cv2.VideoCapture(local+r'\\video\\rose3def_acc.mp4')


                    ret2, frame2 = cap2.read()  
                    mask2 = cv2.inRange(frame2, lower_Blue, upper_Blue) 
                    res2 = cv2.bitwise_and(frame2,frame2, mask= mask2)
                    img2 = cv2.GaussianBlur(mask2,(9,9),10)
                    frame2,eli2 = ellipse(img2,frame2)

                except:

                    pass


            
            if ((time.time() - timer) > 1+treshold and time.time() - timer < 10000):

                treshold = round(time.time() - timer)
                write_cvs(eli0,0)
                list0.append(eli0)
                write_cvs(eli1,1)
                list1.append(eli1)
                write_cvs(eli2,2)
                list2.append(eli2)               

            taille = 0.7

            output(frame0,frame1,frame2)
            
            # If the letter 'q' is pressed closed the program

            if cv2.waitKey(1) & 0xFF == ord('q'):

                os.remove(local +r"\\csv\\data0.csv")
                os.remove(local +r"\\csv\\data1.csv")
                os.remove(local +r"\\csv\\data2.csv")
            
                break

        except KeyboardInterrupt:

            break
    """
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(list0,'-g')
    axs[0, 0].set_title("Fleur 1")
    axs[1, 0].plot(list1,'-r')
    axs[1, 0].set_title("Fleur 2")
    axs[0, 1].plot(list2,'-b')
    axs[0, 1].set_title("Fleur 3")

    fig.tight_layout()
    plt.show()
    """

    cap0.release()
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
