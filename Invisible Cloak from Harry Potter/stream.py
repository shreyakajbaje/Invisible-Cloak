#Import Libraries 

import numpy as np
import cv2

import time  #to give time to set camera

#create video capture object
cap = cv2.VideoCapture(0); #applies to 1.cam 2.video #can use video by putting address over here 

#to setup camera after it is on
time.sleep(2)

#sets background image displayed when cloak is on 
background = 0; 

#step 1: Capturing the background 
for i in range(30):
	ret, background = cap.read() #returns img captured and true if running successful

#step 2: 
while(cap.isOpened()):

	#captures img to work on it
	ret, img = cap.read()

	if not ret:
		break;

	#step 3: converting image from BGR to HSV
	hsv =  cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	#HSV values
	
	#0-10 and 170-180 #saturation-darkness of the colour
	lower_red = np.array([0, 120, 70])
	upper_red = np.array([10, 255, 255])

	#seperating the cloak part 
	mask1 = cv2.inRange(hsv, lower_red, upper_red)

	#0-10 and 170-180 #saturation-darkness of the colour
	lower_red = np.array([170, 120, 70])
	upper_red = np.array([180, 255, 255])

	#seperating the cloak part 
	mask2 = cv2.inRange(hsv, lower_red, upper_red)				

	#if any shade of red will be segmented here and stored in mask1
	mask1 = mask1 + mask2 #OR 1 or x 

	#morphology function removes noise if there
	#noise removal
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
	#gives smoothness to image
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1) 

	#mask2 will be everything of image except the cloak
	mask2 = cv2.bitwise_not(mask1)

	#used for the segmentation of the color
	res1 = cv2.bitwise_and(background, background, mask=mask1)

	#used to substitute the cloak part 
	res2 = cv2.bitwise_and(img, img, mask=mask2)

	#linearly add two images
	final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

	cv2.imshow("Cloak !!", final_output)

	k = cv2.waitKey(10)
	if k == 27:  #when pressed ESC key program should shut down
		break

cap.release()
cv2.destroyAllWindows()