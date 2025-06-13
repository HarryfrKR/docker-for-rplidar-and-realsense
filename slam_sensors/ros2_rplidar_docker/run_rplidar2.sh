docker run -it --rm \
-v /dev:/dev \
--device-cgroup-rule 'c 81:* rmw' \
--device-cgroup-rule 'c 189:* rmw' \
-e DISPLAY="$DISPLAY" \
-e QT_QPA_PLATFORM="xcb" \
-e QT_X11_NO_MITSHM="1" \
-e LIBGL_ALWAYS_INDIRECT="1" \
-e XAUTHORITY="$XAUTHORITY" \
-e NVIDIA_VISIBLE_DEVICES="all" \
-e NVIDIA_DRIVER_CAPABILITIES="all" \
--privileged \
-v /tmp/.X11-unix:/tmp/.X11-unix:rw \
85fe9274e0de bash
