#!/usr/bin/env python3

#For use with normally closed (NC) Reed Switch connected to ground & GPIO input
#If using normally open (NO), simply reverse the booleans.

import RPi.GPIO as GPIO
import time
import smtplib
import _thread
import cred

try:
    need_clean = False

    #Message Template
    #Leading '\n' is required for sending an email with ':' (SMS/MMS Gateway)
    MSG  = '\nDoor was '
    DOOR_MSG = {True:'opened', False:'closed'}

    #Setting up connection to SMTP Server for sending email/sms.
    print('Setting up SMS...')
    #Function to call on new thread
    #Because of race conditions, this needs to be done quickly or on diff thread
    def send_msg(opened:bool):
        #Replace args with your email provider's SMTP details
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login( cred.FROM, cred.PASS )
        #Compile message string to print and send.
        #Ex: '\nDoor was closed at 5:50:20 PM'
        #This way is used because it is quickest and we have race conditions!
        str_print =''.join([MSG, DOOR_MSG[opened], ' at ',
                            time.strftime('%I:%M:%S %p')])
        print(str_print)
        server.sendmail(cred.FROM, cred.TO, str_print)
        server.quit()



    #Initializing GPIO
    print('Setting up hardware...')
    PIN = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #next_state to check for to send message
    next_state = True

    need_clean = True

    #Running actual program
    print('Ready!')
    #Run infinitely
    while True:
        #Check for next state
        if GPIO.input(PIN) == next_state:
            #Send message on different thread
            _thread.start_new_thread(send_msg, (next_state,))
            #Negate next_state
            next_state = not next_state
        time.sleep(0.3)
        
except KeyboardInterrupt:
    GPIO.cleanup() #For Keyboard Interrupt exit
    need_clean = False

if need_clean:    
    GPIO.cleanup() #For normal exit
print('\nEnd!')
