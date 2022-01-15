[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6218246&assignment_repo_type=AssignmentRepo)
/n
In my second project for ENSF 310, I used a Xbox Kinect v2 to track depth data from the middle pixel of the screen using the Pykinect2 library linked below. This data is used to manipulate the brightness of the Nanoleaf wall on the second floor of ICT based on a users proximity to the sensor. This involved learning how to use the library to recieve the desired data from the depth tracking array that is returned from the get_last_depth_frame function and focusing in on the pixel in the middle of the screen, given the depth camera's 424x512 resolution. This project has the following dependencies: ctypes, comtypes, numpy, time, pykinect2, nanoleafapi.

Demo video of the Project will be availible at this link:https://youtu.be/CZaWpaxv8k4

The Kinect python wrappers used for tapping the Microsoft Kinect SDK were provided by the github repo PyKinect v2:https://github.com/Kinect/PyKinect2
Example code was provided by github user valdivj: https://github.com/valdivj/KinectV2_YOLO/blob/master/kinect%20yolo%20depth.py
NOTE: Specifically for the comtypes package dependancy, use comtypes version 1.1.4 as there is a known issue with version conflicts https://github.com/Kinect/PyKinect2/issues/88
