# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    windowName = 'Live Video Feed'
    video_file = "F:\\Projects\\Mine\\Python\\open-cv\\output\\out.avi"
    
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 30
    resolution = (640,480)
    
    VideoFileOut = cv2.VideoWriter(video_file, codec, framerate, resolution)

    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        ret = False

#    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#    
#    plt.imshow(img)
#    plt.show()
        
    while ret:
        ret, frame = cap.read()
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        VideoFileOut.write(output)
        cv2.imshow(windowName, output)
        if cv2.waitKey(1)==27:
            break;
    VideoFileOut.release()
    cap.release()
    cv2.destroyWindow(windowName)

    
if __name__ == "__main__":
   main()
