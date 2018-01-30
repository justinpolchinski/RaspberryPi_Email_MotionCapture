import os
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import smtplib
mail = smtplib.SMTP('smtp.gmail.com',587)

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)
camera = PiCamera()
camera.rotation = 0
print ('Motion Capture Ready')
time.sleep(0)
a=0


while a>=0:
    if a<200:
        m = GPIO.input (4)
        if m > 0:
            
            
            cap = ('/home/pi/Pictures/motion_cap%s.gif')%(a)
            
            print(cap)
            camera.start_preview()
            time.sleep(1)
            camera.stop_preview()
            camera.capture(cap)
            print ("Motion")
            print (m)
            
            content = ("Motion Detected")
            mail = smtplib.SMTP('smtp.gmail.com',587)

            mail.ehlo()

            mail.starttls()

            mail.login('GMAIL GOES HERE', 'Password HERE')
            #from email,receiver of email, content
            
            mail.sendmail('EMAIL TO SEND FROM', 'YOUR_VERIZON_PHONENUMER_HERE@vtext.com', content)
            

            mail.close()
            time.sleep(2)
            a+=1
        
            
            
            
        else:
            print ("Nothing")
            print (m)

            time.sleep (0.1)
    if a==200:
        print ('done')
        break
