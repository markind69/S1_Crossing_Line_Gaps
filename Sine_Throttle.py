from math import sin, cos, radians

pid_Test = rm_ctrl.PIDCtrl()
list_LineList = RmList()
variable_X = 0
variable_T1 = 1
variable_T2 = 0
robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
chassis_ctrl.set_trans_speed(0)
chassis_ctrl.move(0)

# increase 40 to get more wave
for variable_X in range(45, 90):
    variable_T1 = (1 + sin(radians(variable_X * 10)))
    variable_T2 = (1 + cos(radians(variable_X * 10)))
    chassis_ctrl.set_trans_speed(0.5 * variable_T1)
    time.sleep(0.1)
chassis_ctrl.move(0)
