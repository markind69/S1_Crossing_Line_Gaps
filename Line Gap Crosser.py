import math
pid_Test = rm_ctrl.PIDCtrl()
list_LineList = RmList()
variable_X = 0
variable_S = 0
variable_Turned = 0
variable_Turn2 = 0


def re_find_path():
    global variable_X
    global variable_Turned
    global variable_Turn3
    global list_LineList
    global pid_Test
    while not len(list_LineList) == 42:
        gimbal_ctrl.yaw_ctrl(variable_Turn2)
        variable_Turned = variable_Turned + 1
        time.sleep(0.5)
        if variable_Turned > 4:
            gun_ctrl.fire_once()
            variable_Turned = 0
            variable_Turn2 = variable_Turn2 * -1
            chassis_ctrl.set_trans_speed(0.2)
            chassis_ctrl.move_with_distance(0, 0.1)
            time.sleep(0.5)
            chassis_ctrl.stop()
        list_LineList = RmList(vision_ctrl.get_line_detection_info())


def start():
    global variable_X
    global variable_S
    global variable_Turned
    global variable_Turn2
    global list_LineList
    global pid_Test
    variable_Turned = 0
    variable_Turn2 = -5
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    pid_Test.set_ctrl_params(330, 0, 28)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 127, 70, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 161, 255, 69, rm_define.effect_always_on)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    gimbal_ctrl.set_rotate_speed(30)
    gimbal_ctrl.pitch_ctrl(-20)
    while True:
        list_LineList = RmList(vision_ctrl.get_line_detection_info())
        if len(list_LineList) == 42:
            if list_LineList[2] <= 1:
                variable_X = list_LineList[19]
                variable_S = math.sin(variable_X)
                pid_Test.set_error(variable_X - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_Test.get_output(), 0)
                chassis_ctrl.set_trans_speed(0.3)
                chassis_ctrl.move(0)
                time.sleep(0.05)
        else:
            chassis_ctrl.stop()
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
            led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
            time.sleep(2)
            re_find_path()
            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 127, 70, rm_define.effect_flash)
            led_ctrl.set_top_led(rm_define.armor_top_all, 161, 255, 69, rm_define.effect_always_on)
