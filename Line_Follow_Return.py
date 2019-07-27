pid_Test = rm_ctrl.PIDCtrl()
list_LineList = RmList()
variable_X = 0
variable_Turned = 0


def user_defined_re_find_path():
    global variable_X
    global variable_Turned
    global list_LineList
    global pid_Test
    while not len(list_LineList) == 42:
        list_LineList = RmList(vision_ctrl.get_line_detection_info())
        gimbal_ctrl.yaw_ctrl(5)
        time.sleep(0.5)


def start():
    global variable_X
    global variable_Turned
    global list_LineList
    global pid_Test
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    gimbal_ctrl.pitch_ctrl(-20)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    pid_Test.set_ctrl_params(330, 0, 28)
    gimbal_ctrl.set_rotate_speed(30)
    variable_Turned = 0
    while True:
        list_LineList = RmList(vision_ctrl.get_line_detection_info())
        if len(list_LineList) == 42:
            if list_LineList[2] <= 1:
                variable_X = list_LineList[19]
                pid_Test.set_error(variable_X - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Test.get_output(), 0)
                chassis_ctrl.set_trans_speed(0.5)
                chassis_ctrl.move(0)
                time.sleep(0.05)
        else:
            chassis_ctrl.stop()
            gimbal_ctrl.rotate_with_speed(90, -20)
            time.sleep(2)
