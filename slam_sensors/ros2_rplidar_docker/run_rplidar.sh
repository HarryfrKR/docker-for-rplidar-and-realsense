docker run -it --rm \
-v /dev:/dev \
-e NVIDIA_VISIBLE_DEVICES="all" \
-e NVIDIA_DRIVER_CAPABILITIES="all" \
--privileged \
--network host \
rplidar-a1:latest bash
