"""Shared contract constants for the agx_arm_graspgen package.

Scope is intentionally AprilTag-driven for the first milestone. Future
object-frame and learned grasp sources should be added as additional input
streams under `/detections/...` rather than changing this contract.
"""

DEFAULT_INPUT_TOPICS = {
    "detections": "/detections/apriltag",
    "tag_pose": "/detections/tag_pose",
}

DEFAULT_OUTPUT_TOPICS = {
    "grasp_candidates": "/grasp/candidates",
    "debug_markers": "/grasp/debug_markers",
}

# Message types pinned for the cross-package contract.
DETECTION_MSG_TYPE = "apriltag_msgs/msg/AprilTagDetectionArray"
TAG_POSE_MSG_TYPE = "geometry_msgs/msg/PoseStamped"
GRASP_CANDIDATES_MSG_TYPE = "geometry_msgs/msg/PoseArray"
DEBUG_MARKERS_MSG_TYPE = "visualization_msgs/msg/MarkerArray"

DEFAULT_APPROACH_FRAME = "base_link"