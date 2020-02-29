import datetime
import string
from collections import namedtuple

HorizontalDirection = ["WEST","EAST", "NORTH", "SOUTH"]

Rotation = ["LOG_LOCATION_INIT_ON_START_MOVEMENT",
            "LOG_MOVEMENT_ROTATION_MOVEMENT",
            "LOG_MOVEMENT_TURN_IS_FINISHED",
            "LOG_MOVEMENT_TURN_MOVEMENT_START",
            "LOG_GENERAL_DATA"]

KeyWords = ["LOG_STEP_START",
            "LOG_STEP_END",
            "LOG_PROCEDURE_START",
            "LOG_PROCEDURE_END",
            "LOG_ROBOT_MANAGET_EVENT_CHANGE_STATE",
            "STEPS_LEAVE_PARKING",
            "RF COMMUNICATION",
            "STEPS_CLEANING_WIDTHWISE_PREPARE_CLEAN" ,
            "LOG_SENSORS_GAP_DIRECTION_CALIBRATION" ,
            "LOG_MOVEMENT_EDGE_MOVEMENT_START" ,
            "LOG_MOVEMENT_EDGE_MOVEMENT_END",
            "STEPS_CROSS_BRIDGE_CLEAN" ,
            "LOG_SENSORS_GAP_DIRECTION_CALIBRATION",
            "STEPS_CROSS_BRIDGE_PREPARATIONS",
            "LOG_STEP_START_EDGE_MOVE",
            "LOG_MOVEMENT_EDGE_MOVEMENT_START",
            "LOG_MOVEMENT_EDGE_MOVEMENT_END" ,
            "LOG_MOVEMENT_EDGE_MOVEMENT_START" ,
            "STEPS_CLEANING_WIDTHWISE_EDGE_CLEAN" ,
            "STEPS_CLEANING_WIDTHTHWISE_INNER_SEGMENT_CLEAN",
            "STEPS_CLEANING_WIDTHWISE_EDGE_CLEAN_IN_FRAGMENT",
            "(millimeter)",
            "SURFACE_SEGMENT",
            "LOG_COMMUNICATION_RECEIVED",
            "LOG_ROBOT_MANAGER_ERROR",
            "LOG_MOVEMENT_ERROR",
            "LOG_STEP_ERROR",
            "ABORT" ,
            "ABORT_GO_HOME" ,
            "RESPONSE_ERROR_CODE_TELIT_PACKET_RESPONSE_FAILED" ,
            "LOG_LOW_BATTERY"
            "LOG_ROBOT_MANAGER_CHANGE_PARKING_SIDE",
            "LOG_WATCHDOG_STARTED",
            "LOG_COMMUNICATION_INIT_ERROR",
            "LOG_MOVEMENT_TURN_MOVEMENT_START",
            "LOG_MOVEMENT_TURN_IS_FINISHED",
            "LOG_MOVEMENT_INNER_MOVEMENT_START",
            "LOG_ROBOT_STATUS_1",
            "LOG_ROBOT_STATUS_2",
            "LOG_ROBOT_STATUS_3",
            "LOG_COMMUNICATION_RESPONSE",
            "LOG_MOVEMENT_INNER_MOVEMENT_END",
            "LOG_MOVEMENT_REVERSE_MOVEMENT_START",
            "LOG_MOVEMENT_REVERSE_MOVEMENT_END",
            "LOG_MOVEMENT_TURN_MOVEMENT_START",
            "LOG_MOVEMENT_TURN_MOVEMENT_END",
            "LOG_ROBOT_MANAGER_HANDLE_EVENT_CHANGE_STATE"]
class rDirection:
    """description of class"""
    def __init__(self, time,ForwardReverse,direction,dLeft,dRight):
        self.timeStamp = time
        self.go = ForwardReverse
        self.currentDirection = direction
        self.leftEncoderDistance = dLeft
        self.rightEncoderDistance = dRight

class rRotation:
    """description of class"""
    def __init__(self, time,dType,FDirection,TDirection, dLeft,dRight):
        self.timeStamp = time
        self.directionType = dType
        self.fromDirection = FDirection
        self.toDirection = TDirection

