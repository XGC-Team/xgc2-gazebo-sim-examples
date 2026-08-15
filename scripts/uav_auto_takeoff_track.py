#!/usr/bin/env python3
"""Send takeoff, then custom1 once the controller reports Ready/Hover."""
import argparse
import time

import rospy
from std_msgs.msg import String


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ns", default="uav1")
    parser.add_argument("--height", type=float, default=3.0)
    parser.add_argument("--ready-timeout", type=float, default=60.0)
    parser.add_argument("--hover-timeout", type=float, default=40.0)
    args, _ = parser.parse_known_args()

    rospy.init_node("uav_auto_takeoff_track", anonymous=True)
    pub = rospy.Publisher("/command", String, queue_size=1)
    status = {"text": ""}

    def on_status(msg):
        status["text"] = msg.data.strip()

    rospy.Subscriber("/%s/custom/statustext" % args.ns, String, on_status)
    rospy.sleep(0.5)

    deadline = time.time() + args.ready_timeout
    while not rospy.is_shutdown() and time.time() < deadline:
        if status["text"] in ("Ready", "Hover"):
            break
        rospy.sleep(0.2)
    else:
        rospy.logerr("controller never reached Ready (last=%s)", status["text"])
        return

    rospy.loginfo("sending takeoff (status=%s)", status["text"])
    pub.publish(String(data="takeoff"))

    deadline = time.time() + args.hover_timeout
    while not rospy.is_shutdown() and time.time() < deadline:
        if status["text"] == "Hover":
            break
        rospy.sleep(0.2)
    else:
        rospy.logwarn("hover not reached (last=%s); sending custom1 anyway", status["text"])

    rospy.loginfo("sending custom1 (status=%s)", status["text"])
    pub.publish(String(data="custom1"))
    rospy.sleep(0.2)


if __name__ == "__main__":
    main()
