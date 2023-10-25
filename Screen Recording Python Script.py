#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pyautogui


# In[3]:


# Set the screen resolution to record
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

# Customizations
output_filename = "custom_screen_recording.mp4"  # Change the output filename
fps = 24.0  # Adjust the frame rate
left, top, width, height = 100, 100, 800, 600  # Define the region to capture

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Define the recording duration in seconds
recording_duration = 10  # Change this to the desired recording duration

try:
    # Start the screen recording
    for _ in range(int(fps * recording_duration)):
        # Capture the screen within the specified region
        screen = pyautogui.screenshot(region=(left, top, width, height))

        # Convert the screenshot to a numpy array and BGR format for OpenCV
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the output video
        out.write(frame)

    print("Screen recording complete.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Release the VideoWriter
    out.release()

