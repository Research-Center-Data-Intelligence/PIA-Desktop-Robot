from InputOutputPia import *

def Main(): 
    # Make an instance of the class
    touchSensor = TouchSensor()
    vibrationSensor = VibrationSensor()

    leftArmServoMotor = ServoMotor(0)
    rightArmServoMotor = ServoMotor(1)
    bodyServoMotor = ServoMotor(2)

    display = LcdDisplay()


    while True:
        if touchSensor.Is_Touched:
            display.show_image('./pic/eyes/Eyes_Touched.jpg')

            leftArmServoMotor.set_angle(0)
            rightArmServoMotor.set_angle(0)
            time.sleep(0.5)
            
            for x in range(3):
                leftArmServoMotor.set_angle(50)
                rightArmServoMotor.set_angle(50)
                time.sleep(0.25)
                leftArmServoMotor.set_angle(0)
                rightArmServoMotor.set_angle(0)


        elif vibrationSensor.Is_Vibrating:
            display.show_image('./pic/eyes/Eyes_Angry_1.jpg')

            leftArmServoMotor.set_angle(0)
            rightArmServoMotor.set_angle(0)
            bodyServoMotor.set_angle(0)

            time.sleep(0.5)
            leftArmServoMotor.set_angle(180)
            rightArmServoMotor.set_angle(180)

            time.sleep(0.5)
            leftArmServoMotor.set_angle(0)
            rightArmServoMotor.set_angle(0)

            display.show_image('./pic/eyes/Eyes_Angry_2.jpg')

            time.sleep(0.5)
            leftArmServoMotor.set_angle(180)
            rightArmServoMotor.set_angle(180)

            time.sleep(0.5)
            leftArmServoMotor.set_angle(0)
            rightArmServoMotor.set_angle(0)
            
        else:
            display.show_image('./pic/eyes/Eyes_Default.jpg')

Main()






