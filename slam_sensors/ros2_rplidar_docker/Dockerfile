FROM ros:humble-ros-base

SHELL ["/bin/bash", "-c"]

ENV ROS_DISTRO=humble
ENV DEBIAN_FRONTEND=noninteractive

# Install required dependencies
RUN apt-get update && apt-get install -qq -y --no-install-recommends \
    git \
    cmake \
    build-essential \
    pkg-config \
    curl \
    python3-colcon-common-extensions \
    python3 \
    python3-pip \
    ros-${ROS_DISTRO}-ament-cmake \
    ros-humble-rmw-cyclonedds-cpp \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws

# Install ROS 2 dependencies
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    apt-get update -y \
 && apt-get install -y \
    ros-${ROS_DISTRO}-rviz2 \
 && mkdir src \
 && cd src \
 && git clone https://github.com/Slamtec/sllidar_ros2 \
 && cd .. \
 && apt-get install -y python3-rosdep \
 && source /opt/ros/${ROS_DISTRO}/setup.bash \
 && rm /etc/ros/rosdep/sources.list.d/20-default.list \
 && rosdep init \
 && rosdep update \
 && rosdep install --from-paths src --ignore-src -r -y \
 && colcon build --symlink-install

# Source the workspace setup in the container's environment
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Set entrypoint
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && source /ros2_ws/install/setup.bash && bash"]

# ENV DEBIAN_FRONTEND=dialog
# ENV ROS_DOMAIN_ID=42
# ENV ROS_LOCALHOST_ONLY=0
# ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# CMD [ "rs-enumerate-devices", "--compact" ]
