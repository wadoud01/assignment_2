# Description of the program
ROS is an open-source framework for developing and managing robotic systems that provides a set of tools and libraries for creating complex robotic applications. It includes publisher and subscriber for sending and receiving data, action client for requesting and receiving results from a server, launch file for starting and configuring nodes, custom service for creating new request-response pattern and custom message for sending data between nodes. These features enable communication between different parts of a robotic system, making it easy to create, test and launch complex robotic applications.
## USED PACKAGES:
- Scripts : contains node a, b, c
- msg : costumised msg counter.msg 
- launch.file : Contains launch.file that starts all the node and the world simulator

## USED NODES:
- Control: represents node (a) which is responsible for to retreive from the use cordination x and y. then set a goal and send the information to the msg
- rob_info: this actually the node b and it responsible to request the paramters of the position, then calculate the average_speed under the frequancy of 1.0
- Counter : node (c) node responsible for calculating the number of the goals that has been reached and cancled.
all these 3 nodes are located in assignment_2_2022/scripts

## CUSTOMITED SERVICE: 
"The file, count.srv, located in assignemnt_2_2022/srv, is designed to take in canceled and reached goals by the robot and the user.
## CUSTOMITED Message: 
"The file, vel_position, located in /msg, is designed to take in two float32 requests, the user input the desired position X and Y of the robot, then return a float32 response, So it can used by the node (b) to calculate the distance and the average velocity assigned by the robot."
## How to run it?
to run the ROS you need first to build the world by inserting catkin_make then you can launch the ROS by just pressing assignment_2_2022 assignment1.launch
#How to use the user interface
The use is asked to insert the desired position X and Y. or in case wanna cancel just press "Cancel"
# Flowchart of our program
These are the following fllow chart in order. 
- node(a) : represents the control.py node which takes the position x and y from the user.
- node(b) : rob_info.py which responsible for calculating the averge speed and distance. (note in first desicion the arrow should go the next desicion we appologies abouthe mistake) 
- node(c) : counter.py resiponsilbe for counting number of goals reached and canceled.

![node (a)](https://user-images.githubusercontent.com/116806672/214814681-9e90a58f-83cc-4230-bad3-3b447b598840.png)
![node(b)](https://user-images.githubusercontent.com/116806672/214817145-d0bdd66c-c59b-4708-b713-eab89ec3239a.png)
![node(c)](https://user-images.githubusercontent.com/116806672/214814727-d013ac3e-eb26-476a-8f21-3b74f64375bc.png)
