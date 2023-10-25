# Screen Recording Python Script

## Overview
This Python script allows you to record your screen using OpenCV and PyAutoGUI. It captures the screen in real-time, and you can customize the output filename, recording duration, frame rate, and the region of the screen you want to record.

## Usage
1. **Prerequisites**:
   - Python 3.x
   - OpenCV (`pip install opencv-python`)
   - PyAutoGUI (`pip install pyautogui`)

2. **Customization**:
   - **Output Filename**: You can change the output filename by modifying the `output_filename` variable in the script.

   - **Recording Duration**: Adjust the `recording_duration` variable to set the desired recording duration in seconds.

   - **Frame Rate (FPS)**: Change the `fps` variable to adjust the frame rate of the recording.

   - **Capture a Specific Region**: Modify the `left`, `top`, `width`, and `height` variables to define the region of the screen you want to capture.

3. **Running the Script**:
   - Execute the script using Python: `python screen_recording.py`

4. **Error Handling**:
   - The script includes basic error handling to catch exceptions. If an error occurs during the recording, the script will print an error message.

## Additional Details
- This project is designed to create screen recordings for a variety of purposes, including tutorials, presentations, and demonstrations.
- You can easily modify the script to capture a specific region of the screen or record the entire screen.
- The captured video is saved in MP4 format, but you can change the codec and file extension to suit your preferences.
- Feel free to customize the code and use it for your own screen recording needs.

For any questions, issues, or contributions, please open an issue in the GitHub repository.

Enjoy recording your screen with this simple Python script!
