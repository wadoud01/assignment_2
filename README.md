# Description of the program

## USED PACKAGES:
- Scripts : contains node a, b, c
- msg : costumised msg counter.msg 
- launch.file : Contains launch.file that starts all the node and the world simulator

## SED NODES:
- Control: is the node responsible for to retreive from the use cordination x and y. then set a goal and send the information to the msg
- rob_info: this actually the node b and it responsible to request the paramters of the position, then calculate the average_speed under the frequancy of 1.0
- Counter : node (c) node responsible for calculating the number of the goals that has been reached and cancled.
all these 3 nodes are located in assignment_2_2022/scripts
## CUSTOMITED SERVICE: 
created in my_srv/srv/Velocity.srv has two float32 requests and one float32 response the two requestes are : the user input and the current velocity of the robot the response : the new velocity multiplier assigned to the robot
## CUSTOMITED SERVICE: 
created in assignment_2_2022/srv/count.srv has two float32 requests and one float32 response the two requestes are : the user input and the current velocity of the robot the response : the new velocity multiplier assigned to the robot
## CUSTOMITED Message: 
created in assignment_2_2022/srv/count.srv has two float32 requests and one float32 response the two requestes are : the user input and the current velocity of the robot the response : the new velocity multiplier assigned to the robot
#How to run it?
to run the ROS you need first to build the world by inserting catkin_make then you can launch the ROS by just pressing assignment_2_2022 assignment1.launch
#How to use the user interface
The use is asked to insert the desired position X and Y. or in case wanna cancel just press "Cancel"
#Flowchart of our program
The flow chart will sent by an email.

