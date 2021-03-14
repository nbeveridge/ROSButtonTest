FROM ros:noetic

RUN apt-get update
#RUN apt-get install python3-dev python3-rpi.gpio
RUN apt-get install python3-dev

Run  apt-get install dos2unix

####################################################################
# RUN apt-get -y install python3-pip

# RUN pip3 install py-getch

# RUN pip3 install readkeys

# RUN pip3 install keyboard
####################################################################

RUN mkdir -p catkin_ws/src

RUN . /opt/ros/noetic/setup.sh && catkin_init_workspace /catkin_ws/src
RUN . /opt/ros/noetic/setup.sh && cd /catkin_ws && catkin_make
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

RUN cd catkin_ws/src && catkin_create_pkg scripts

COPY distal_balloon_node_sub.py catkin_ws/src/scripts
COPY distal_balloon_sensor_node_pub.py catkin_ws/src/scripts
COPY controller_node_pub_sub.py catkin_ws/src/scripts
COPY user_command_node_pub.py catkin_ws/src/scripts

RUN dos2unix catkin_ws/src/scripts/distal_balloon_node_sub.py
RUN dos2unix catkin_ws/src/scripts/distal_balloon_sensor_node_pub.py
RUN dos2unix catkin_ws/src/scripts/controller_node_pub_sub.py
RUN dos2unix catkin_ws/src/scripts/user_command_node_pub.py

RUN cd catkin_ws/src/scripts && chmod +x distal_balloon_node_sub.py
RUN cd catkin_ws/src/scripts && chmod +x distal_balloon_sensor_node_pub.py
RUN cd catkin_ws/src/scripts && chmod +x controller_node_pub_sub.py
RUN cd catkin_ws/src/scripts && chmod +x user_command_node_pub.py

COPY test.launch catkin_ws/src/scripts
RUN cd catkin_ws/src/scripts && chmod +x test.launch

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

RUN ln -s /usr/bin/python3 /usr/bin/python

CMD ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /catkin_ws/devel/setup.bash && roslaunch scripts test.launch"]
