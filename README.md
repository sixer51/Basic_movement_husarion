# cs169_yijia_pa1

## Implementation
1. task1  
I implemented a node "move" as a publisher to publish Twist message to topic `cmd_vel`. Inside the task1.py script, a function forward(forward_velocity, distance) can be used to control the movement velocity and distance. A task1.launch file is also implemented to start all sensors and run task1.py at the same time.

2. task2  
I implemented a launch file which can start all the sensors of the robot, run the file implemented for task one to move forward and record all topics with rosbag. All topics exclude the image_raw is included to be recorded to the bags folder.

3. task3  
I implemented a node "get_position" as a subscriber of topic `pose`(type: geometry_msgs/Pose_Stamped) and a publisher of topic `marker`(type: visulaization_msgs/Marker).

## Performance
1. task1  
After running task1.launch, the robot can publish Twist message to topic `cmd_vel` to move forward for a distance with the velocity set in function forward. 

2. task2  
In this task, at first, when I run the task2.launch, the robot can run the same distance as that in the task1 and record the bag at the same time, but I didn't do the experiemnt on the ground at that time. It could work until last night, but after some modification, it stopped working anymore. The robot cannot run and record the bag at the same time. I used several possible solutions:   
(1) let the robot sleep for several seconds before moving forward to give it enough time to initialize   
(2) change the publish rate to different values from 1hz to 100hz  
(3) delete all previous bag file to make sure there are enough room to save the new bag  
It sometimes works, but usually doesn't. Another problem is that it is hard to use `ctrl+c` to stop it. I need to press for several seconds to stop it which also make the bag file broken, so all bag I recorded are followed with ".active". It can be repaired with `rosbag reindex <bag_file>`, but it doesn't seem like a proper way to go. Sometimes I can also see some warning saying buffer exceed and there are error about compressed image all the time. These might be the reasons that influence the movement of the robot.

3. task3  
After running task3.launch, we can see a new topic "marker" in rostopic list and visualize it in rviz. When the robot move forward, the marker will also move in rviz which proves that the node successfully subscribed to `pose` topic.
