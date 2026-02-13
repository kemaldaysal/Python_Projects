import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def watershed():
    imgPath = os.path.join('Image_Processing/Test_Scripts/Watershed_Segmentation/Image_Inputs/joshua_tree_2.jpeg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    plt.figure()
    plt.subplot(231)
    plt.imshow(img,cmap='gray')
    
    ## Thresholding - Initial Extraction of the Tree
    
    plt.subplot(232)
    p_thresh_min = 80
    p_thresh_max = 255
    p_threshold_method = cv.THRESH_BINARY_INV
    _,imgThreshold = cv.threshold(img, p_thresh_min, p_thresh_max, p_threshold_method)
    plt.imshow(imgThreshold, cmap='gray')
    
    ## Dilation - To improve categorization, remove - reduce black areas before doing distance transform
    plt.subplot(233)
    p_kernel_size_one_axis = 3
    p_kernel = np.ones((p_kernel_size_one_axis,p_kernel_size_one_axis), np.uint8)
    imgDilated = cv.morphologyEx(imgThreshold, cv.MORPH_DILATE, p_kernel)
    plt.imshow(imgDilated)
    
    ## Distance Transform - Find the distance from the current pixel to the nearest black (0) pixel and draw a heatmap
    # Helps finding the center of the different regions
    plt.subplot(234)
    p_dist_type = cv.DIST_L2 # Simple Eucledian Distance (Recommended in function helper)
    p_mask_size = 3 # alternatives: 0, 3, 5
    distTransform = cv.distanceTransform(imgDilated, p_dist_type, p_mask_size) 
    plt.imshow(distTransform)
    
    # Before using the connected components, we have to do some thresholding to further isolate the areas  
    plt.subplot(235)
    p_thresh_min = 15
    p_thresh_max = 255
    p_threshold_method = cv.THRESH_BINARY    
    _,distThreshold = cv.threshold(distTransform, p_thresh_min, p_thresh_max, p_threshold_method)
    plt.imshow(distThreshold)
    
    ## Connected Components - Find the different regions and number them into different areas using labels
    plt.subplot(236)
    distThreshold = np.uint8(distThreshold)
    _,labels = cv.connectedComponents(distThreshold)
    plt.imshow(labels)
    
    ## Run the Watershed
    
    plt.figure()
    
    plt.subplot(131)
    plt.imshow(imgRGB)     
    
    plt.subplot(132)
    labels = np.int32(labels)
    labels = cv.watershed(imgRGB, labels)
    plt.imshow(labels)
    
    plt.subplot(133)
    imgRGB_highlighted = imgRGB
    imgRGB_highlighted[labels==-1] = [255,0,0] ## labels==-1 are edges, highlight the edges as red
    plt.imshow(imgRGB) 
    
    plt.show()
    

if __name__ == '__main__':
    watershed()

