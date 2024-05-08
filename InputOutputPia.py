import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import logging
from lib import LCD_2inch
from PIL import Image
#from picamera import PiCamera
from time import sleep
#import cv2 
import time


class TouchSensor:
    def __init__(self):
        # Define the GPIO pin to which the capacitive touch sensor is connected
        self.touch_sensor_pin = 16  # You can change this to the actual GPIO pin you're using

        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.touch_sensor_pin, GPIO.IN)

    @property
    def Is_Touched(self):
        if GPIO.input(self.touch_sensor_pin) == 1:
            return True
        else:
            return False

class VibrationSensor:
    def __init__(self):
        self.vibration_sensor_pin = 22    # Define the GPIO pin Indien verkeerde pin, return altijd true indien verkeerde pin

    # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.vibration_sensor_pin, GPIO.IN)

    @property
    def Is_Vibrating(self): #Function to call the test for checking the functionality of the vibration sensor
        if GPIO.input(self.vibration_sensor_pin) == 1:
            #print("Vibration detected!") 
            return True
        else:
            return False
 
class ServoMotor:
    def __init__(self, Servo_index):
        self.kit = ServoKit(channels=16)

        # Define the servo channels
        if Servo_index == 0: #Index voor de specicific motors in P.I.A.
            self.servo_channel = 0 #Connections to Adafruit Servo Channel (0-16)
        elif Servo_index == 1: 
            self.servo_channel = 2 
        elif Servo_index == 2: 
            self.servo_channel = 4 
        else:
            raise ValueError("Invalid motor index")
        

    def set_angle(self, angle):
        self.kit.servo[self.servo_channel].angle = angle
        
    # def ServoTest():
    #     kit = ServoKit(channels=16)
    #     LeftArm  = 0
    #     RightArm = 2
    #     BodyTurn = 4

    #     def set_servo_position(channel, angle):
    #         kit.servo[channel].angle = angle

    #     try:
    #         print("Servo motor testing. Press Ctrl+C to exit.")
    #         while True:
    #             # Move servo 1
    #             set_servo_position(LeftArm, 0)  # Move to 0 degrees
    #             time.sleep(2)
    #             set_servo_position(LeftArm, 180)  # Move to 90 degrees
    #             time.sleep(0.5)

    #             # Move servo 2
    #             set_servo_position(RightArm, 45)  # Move to 45 degrees
    #             time.sleep(2)
    #             set_servo_position(RightArm, 135)  # Move to 135 degrees
    #             time.sleep(0.5)

    #             # Move servo 3
    #             set_servo_position(BodyTurn, 180)  # Move to 180 degrees
    #             time.sleep(1)
    #             set_servo_position(BodyTurn, 0)  # Move to 0 degrees
    #             time.sleep(1)
    #     except KeyboardInterrupt:
    #         print("\nTesting ended. Cleaning up.")
    #         # Center all servos before cleanup
    #         set_servo_position(LeftArm, 90)
    #         set_servo_position(RightArm, 90)
    #         set_servo_position(BodyTurn, 90)
    #         kit.servo[0].angle = None
    #         kit.servo[1].angle = None
    #         kit.servo[2].angle = None

class LcdDisplay:
    def __init__(self):
        # Raspberry Pi pin configuration:
        RST = 27
        DC = 25
        BL = 18
        bus = 0 
        device = 0 

        try:  
            self.disp = LCD_2inch.LCD_2inch()  # Create display object
            self.disp.Init() # Initialize library.
            self.disp.clear()  # Clear display.
            self.disp.bl_DutyCycle(50)   #Set the backlight to 100

            # Show the default eye image
            image = Image.open('./pic/LCD_2inch_eye.jpg')	# You can Add JPG's in the Pic lib
            self.disp.ShowImage(image)

            # Exit module 
            # self.disp.module_exit()
        except IOError as e:
            logging.info(e)    
        # except KeyboardInterrupt:
        #     self.disp.module_exit()

    def show_image(self, imageFileName):
        # Show the default eye image
        image = Image.open(imageFileName)	# You can Add JPG's in the Pic lib
        self.disp.ShowImage(image)
        
    # exit()
        

    #Open for additions, currenntly no speakers implented

# #class RpiCamera: #Problems with integrating camera due to remote control, left out for now.
#     print("RPI camera")

#     def show_webcam():  
#         while True:
#          # Open the default camera (index 0)
#          #   cams = get_available_webcams()
#          #   print(cams)
#             cap = cv2.VideoCapture("rtsp://raspberry:raspberry@192.168.137.175/video")

#          # Capture frame-by-frame
#         ret, frame = cap.read()

#          # Display the resulting frame
#         if frame != None:
#              cv2.imshow('Webcam Feed', frame)

#          # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             #break

# #    Release the camera and close the window
# #    cap.release()
# #    cv2.destroyAllWindows()
# #    def get_available_webcams():
# #       available_webcams = []
# #       index = 0

#         #while True:
#             cap = cv2.VideoCapture(index)
#         if not cap.read()[0]:
#         #    break
#         #else:
#             available_webcams.append(index)
#         cap.release()
#         index += 1
#     #return available_webcams

#     if __name__ == '__main__':
#         show_webcam()

#     camera = PiCamera()

#     camera.start_preview()
#     sleep(5)
#     camera.stop_preview()