import rospy
import statistics
from geometry_msgs.msg import PoseStamped
import pandas as pd

y_pose = []
x_pose = []
x_ortientation = []
z_ortientation = []
y_ortientation = []


y_pose.clear()
x_pose.clear()
def callback(pose):
 
    try:
        x_ilk = x_pose[0]
        x_son = float(x_pose[-1:])
        print(float(x_pose[-1:])-float(x_pose[0]))
        
    except:
        print("bekle")
    y_pose.append(pose.pose.position.y)
    x_pose.append(pose.pose.position.x)
    x_ortientation.append(pose.pose.orientation.x)
    y_ortientation.append(pose.pose.orientation.y)
    z_ortientation.append(pose.pose.orientation.z)

    data = {'Konum X':x_pose,'Konum Y':y_pose,'Oryantasyon X':x_ortientation,'Oryantasyon Y':y_ortientation,'Oryantasyon Z':z_ortientation}
    df = pd.DataFrame(data)
    df.to_csv('/home/gursel/Desktop/y_pose.csv', index=False)
    df_saved_file = pd.read_csv('/home/gursel/Desktop/y_pose.csv')

    
        
               
def listener():
    rospy.init_node("Oret_pose")
    rospy.Subscriber("/mavros/local_position/pose",PoseStamped,callback)
    rospy.spin()
if __name__ == '__main__':
    listener()

