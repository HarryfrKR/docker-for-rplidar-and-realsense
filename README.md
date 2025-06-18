# Docker file for RPLiDAR and Realsense
Verified with following HW : 
* Jetson Orin Nano with Jetpack 6 or lower-5.13 (Ubuntu 22.04)
* Raspberry 5 (Ubuntu 24.04 LTS)

# How to run
## prerequisites
Docker v28.0.1

## Build docker containers
1. Go to ros2_rplidar_docker folder and run ```docker build -t rplidar:latest .```
2. Go to ros2_realsense_docker folder and run  ```docker build -t realsense-camera:latest .```
3. (Optional) If you want to run the docker container seperately, run ```./run_<sensor_name>``` in each folder after making the script executable with ```chmod +x /path/to/run_<sensor_name>```

## Run both sensors with docker compose
1. Make sure that RPLidar and Realsense are connected to the board/computer (minimum USB 3.0 for realsense)
2. Change the launch command ```ros2 launch sllidar_ros2 sllidar_c1_launch.py``` in docker-compose.yml file if you have another RPLiDAR model 
3. Run ``` docker compose up ``` in slam-sensors folder
