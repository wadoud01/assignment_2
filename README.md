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
The flow chart will sent by an email.

![node (a)](https://user-images.githubusercontent.com/116806672/214813927-72824735-a301-46f1-91bd-808334128c2a.png)
![node(b)](https://user-images.githubusercontent.com/116806672/214813943-053b7fc3-9c56-42e5-87c2-b88ca266c709.png)
![node(c)](https://user-images.githubusercontent.com/116806672/214813981-98842db3-3d4e-4d72-9b84-32ae2f706997.png)


