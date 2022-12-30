import RPi.GPIO as GPIO


def button_callback_dup(channel):
    print ("This is D-Pad Up")
def button_callback_dleft(channel):
    print ("This is D-Pad Left")
def button_callback_ddown(channel):
    print ("This is D-Pad Down")
def button_callback_dright(channel):
    print ("This is D-Pad Right")
def button_callback_red(channel):
    print ("This is the Big Red Button")
def button_callback_green(channel):
    print ("This is the Small Green Button")
def button_callback_blue(channel):
    print ("This is the Blue Triangle Button")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.add_event_detect(6,GPIO.FALLING,callback=button_callback_dright, bouncetime=300)
GPIO.add_event_detect(16,GPIO.FALLING,callback=button_callback_dup, bouncetime=300)
GPIO.add_event_detect(25,GPIO.FALLING,callback=button_callback_ddown, bouncetime=300)
GPIO.add_event_detect(5,GPIO.FALLING,callback=button_callback_dleft, bouncetime=300)
GPIO.add_event_detect(17,GPIO.FALLING,callback=button_callback_blue, bouncetime=300)
GPIO.add_event_detect(27,GPIO.FALLING,callback=button_callback_green, bouncetime=300)
GPIO.add_event_detect(22,GPIO.FALLING,callback=button_callback_red, bouncetime=300)

message = input("Press enter to quit\n\n")
GPIO.cleanup()