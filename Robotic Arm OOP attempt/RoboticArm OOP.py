from motor_class import Motor


motor1_wait_ms=20
motor2_wait_ms=90
motor3_wait_ms=20
motor5_wait_ms=20
motor6_wait_ms=1000

motor_wait_list=[motor1_wait_ms,motor2_wait_ms,motor3_wait_ms,motor5_wait_ms,motor6_wait_ms]
motor1 = Motor(15,50,100,0,0,180)
motor2 = Motor(8,40,20,0,30,30)
motor3 = Motor(7,120,165,140,160,150)
motor5 = Motor(5,160,110,0,110,110)
motor6 = Motor(6,180,90,0,90,180)

motor_list=[motor1,motor2,motor3,motor5,motor6]

for i in range(len(motor_list)):
    motor_list[i].move_motor(motor_list[i].start,motor_list[i].conveyor,motor_wait_list[i])
motor3.move_motor(motor3.conveyor,motor3.conveyor_adjustment,motor3_wait_ms)
motor3.conveyor=motor3.conveyor_adjustment


for i in range(len(motor_list)):
    motor_list[i].move_motor(motor_list[i].conveyor,motor_list[i].color,motor_wait_list[i])

for i in range(len(motor_list)):
    motor_list[i].move_motor(motor_list[i].color,motor_list[i].storing,motor_wait_list[i])

for i in range(len(motor_list)):
    motor_list[i].move_motor(motor_list[i].storing,motor_list[i].start,motor_wait_list[i])
