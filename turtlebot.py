#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TurtleBotNavigator(Node):

    def __init__(self):
        super().__init__('turtlebot_navigator')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.scan_subscriber_ = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
        self.msg_ = Twist()

    def scan_callback(self, msg):
        min_dist = min(msg.ranges)
        if min_dist < 0.5:
            # Obstacle detected, rotate until clear
            self.msg_.linear.x = 0.0
            self.msg_.angular.z = 0.5
        else:
            # No obstacle detected, move forward
            self.msg_.linear.x = 0.5
            self.msg_.angular.z = 0.0
        self.publisher_.publish(self.msg_)

def main(args=None):
    rclpy.init(args=args)
    turtlebot_navigator = TurtleBotNavigator()
    rclpy.spin(turtlebot_navigator)
    turtlebot_navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
