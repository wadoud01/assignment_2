#! /usr/bin/env python

import rospy
from assignment_2_2022.srv import count, goal_srvResponse
import actionlib
import actionlib.msg
import assignment_2_2022.msg

cancelled_goals = 0 #intilaize which represents Canceled goals 
reached_goals = 0 #initilize which represnets Reached goals

def result_callback(msg):
    global cancelled_goals, reached_goals
    state = msg.status.status
    if state == 2:
        cancelled_goals += 1
        rospy.loginfo("Number of goal canceled is {:.1f}".format(cancelled_goals))
    elif state == 3:
        reached_goals += 1
        rospy.loginfo("Number of goal reached is {:.1f}".format(reached_goals))

def info_callback(req):
    global cancelled_goals, reached_goals
    rospy.loginfo("Number of goal canceled is {:.1f} and Number of goal reached is {:.1f}".format(cancelled_goals, reached_goals))
    return goal_srvResponse()

if __name__ == "__main__":
    rospy.init_node('counter') #intializing the node counter 
    sub_result = rospy.Subscriber('/reaching_goal/result_callback', assignment_2_2022.msg.PlanningActionResult, result_callback) #subscribing to the result topic
    srv = rospy.Service('counter', count, info_callback)
    rospy.spin() #spin to handle callbacks

