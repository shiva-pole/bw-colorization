# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt

def main():
    windowName = 'Live Video Feed'
    video_file = "F:\\Projects\\Mine\\Python\\open-cv\\output\\out.avi"
    
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(video_file)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

#    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#    
#    plt.imshow(img)
#    plt.show()
        
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(33)==27:
                break
        else:
            break
            
    cap.release()
    cv2.destroyWindow(windowName)

    
if __name__ == "__main__":
   main()
