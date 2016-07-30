#!/usr/bin/env python
import rospy
import std_msgs.msg 
import visualization_msgs.msg as vm
import geometry_msgs.msg as gm

def clear():
    pub = rospy.Publisher('visualization_marker',vm.Marker,latch=True,queue_size=10)
    if not rospy.is_shutdown():
        m=vm.Marker()
        m.type = m.SPHERE_LIST
        m.action = m.DELETE
        pub.publish(m)

def talker():
    pub = rospy.Publisher('visualization_marker',vm.Marker,latch=True,queue_size=10)
    #pub = rospy.Publisher('visualization_marker_array',vm.MarkerArray,latch=True,queue_size=10)

    #rospy.init_node('waypoint_course', anonymous=True)
    rospy.init_node('waypoint_course')    
    
    if not rospy.is_shutdown():
        XX = [0,2,-2,-2,2]
        YY = [0,2,2,-2,-2]
        m=vm.Marker()
        m.type = m.SPHERE_LIST
        m.action = m.MODIFY
        s=0.2
        m.scale.x = s
        m.scale.y = s
        m.scale.z = s
        m.color.r=1.0
        m.color.g=0
        m.color.a=1.0
        m.header.stamp = rospy.Time.now()
        m.header.frame_id = "odom"
        for x,y,mid in zip(XX,YY,range(len(XX))):
            p = gm.Point()
            p.x =x
            p.y =y
            m.points.append(p)

        print("Publishing Sphere List")
        pub.publish(m)
      
      

if __name__ == '__main__':

    try:
        #clear()
        talker()
    except rospy.ROSInterruptException:
        pass
