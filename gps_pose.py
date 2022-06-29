import rospy
import statistics
from geometry_msgs.msg import PoseStamped
import pandas as pd

y_pose = []
avg_list = []
y_pose.clear()
def callback(pose):
    y_pose.append(pose.pose.position.y)
    avg = round(statistics.mean(y_pose[-10:]),2) 
    avg_list.append(avg)
    df2 = pd.DataFrame(avg_list)
    df = pd.DataFrame(y_pose)
    df.to_csv('/home/gursel/Desktop/y_pose.csv', index=False)
    df_saved_file = pd.read_csv('/home/gursel/Desktop/y_pose.csv')

    df2.to_csv('/home/gursel/Desktop/avg_list.csv', index=False)
    df2_saved_file = pd.read_csv('/home/gursel/Desktop/avg_list.csv')
    #pub.publis(avg) #BUNU PULISH EDECEKSIN
        
               
def listener():
    rospy.init_node("Oret_pose")
    rospy.Subscriber("/mavros/local_position/pose",PoseStamped,callback)
    rospy.spin()
if __name__ == '__main__':
    listener()

