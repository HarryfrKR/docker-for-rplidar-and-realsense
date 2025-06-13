from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch RealSense Docker Container
        ExecuteProcess(
            cmd=[
                "docker", "run", "-it", "--rm",
                "-v", "/dev:/dev",
                "--device-cgroup-rule", "c 81:* rmw",
                "--device-cgroup-rule", "c 189:* rmw",
                "--network", "host",
                "-e", "NVIDIA_VISIBLE_DEVICES=all",
                "-e", "NVIDIA_DRIVER_CAPABILITIES=all",
                "-e", "RMW_IMPLEMENTATION=rmw_cyclonedds_cpp",
                "--privileged",
                "realsense-camera:latest",
                "ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true"
            ],
            shell=True,
            output='screen'
        ),

        # Launch RPLIDAR Docker Container
        ExecuteProcess(
            cmd=[
                "docker", "run", "-it", "--rm",
                "-v", "/dev:/dev",
                "-e", "NVIDIA_VISIBLE_DEVICES=all",
                "-e", "NVIDIA_DRIVER_CAPABILITIES=all",
                "--privileged",
                "--network", "host",
                "rplidar-a1:latest",
                "ros2 launch sllidar_ros2 sllidar_c1_launch.py"
            ],
            shell=True,
            output='screen'
        ),

        # Static Transform Publisher for RealSense D435i to LIDAR
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0.1', '0', '0', '0', 'camera_link', 'laser_frame'],
            output='screen'
        )
    ])
