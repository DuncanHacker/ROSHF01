from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    # Create the node
    navigator_node = Node(
        package="ros2_course",
        executable="turtlebot",
        name="turtlebot"
    )
    
    # Add the node to the launch description
    ld.add_action(navigator_node)
    
    return ld
   
if __name__ == '__main__':
	generate_launch_description()

