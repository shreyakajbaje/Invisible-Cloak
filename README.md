# Invisible-Cloak
Invisible Cloak from Harry Potter

## Overview
  This is Invisible Cloak from Harry Potter developed in Python. The camera of the device will be used to capture the images and 
  instead a link of video can be given. Initially the background will be captured by camera after turning it on and the red cloak 
  should appear after that. The red cloak will be captured and will be made transparent to background using numpy and cv2 libraries.
  The code is well commented for better understanding.
    
## Built with
  - Python
  - numpy library
  - cv2 library

## Key Concepts

Step 1:                                                                                                                        
  Capturing the background.                                                                                 
Step 2:                                                                                                   
  Capture image to work on it.                                                                                                          
Step 3:                                                                                                            
  Converting image from BGR to HSV                                                                                                    
Step 4:                                                                                                          
  Morphology function removes noise if there and gives smoothness.                                                                                                             
Step 5:                                                           
  Segmentation of color and substitute the cloak part.                                                   
Step 6:                                               
  Linearly add two images.                                                      
  
## Steps to run

1.Pull down the code locally.                
2.Open Downloaded file.                                        
3.Unzip the downloaded file.                                            
4.Inside locate "stream.py" file.                                                        
5.Run the file using cmd.                                          
