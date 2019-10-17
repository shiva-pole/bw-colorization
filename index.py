# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import matplotlib.pyplot as plt

def main():
    print("main function")
    img_path = "F:\\Projects\\Mine\\Python\\open-cv\\Dataset\\4.2.04.tiff";
    img = cv2.imread(img_path,1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.show()
    
#    cv2.imshow('Lena', img)
#    cv2.waitKey(0)
#    cv2.destroyWindow('Lena')
    
    
if __name__ == "__main__":
    main()
