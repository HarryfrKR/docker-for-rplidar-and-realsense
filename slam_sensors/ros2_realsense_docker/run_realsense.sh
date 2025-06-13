docker run -it --rm \
-v /dev:/dev \
--device-cgroup-rule 'c 81:* rmw' \
--device-cgroup-rule 'c 189:* rmw' \
--network host \
-e NVIDIA_VISIBLE_DEVICES="all" \
-e NVIDIA_DRIVER_CAPABILITIES="all" \
-e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
--privileged \
realsense-camera:latest bash

