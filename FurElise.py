import RPi.GPIO as GPIO
import time

NoteE =
NoteDs = 
NoteB = 
NoteC = 
NoteA = 
NoteGs = 
NoteD = 

GPIO.setmode(GPIO.BCM)

GPIO.setup(NoteE,GPIO.OUT)
GPIO.setup(NoteDs,GPIO.OUT)
GPIO.setup(NoteB,GPIO.OUT)
GPIO.setup(NoteC,GPIO.OUT)
GPIO.setup(NoteA,GPIO.OUT)
GPIO.setup(NoteGs,GPIO.OUT)

def E():
                GPIO.output(NoteE,GPIO.HIGH)
                time.sleep(.5)
                
def Ds():
                GPIO.output(NoteDs,GPIO.HIGH)
                time.sleep(.5)

def B():
                GPIO.output(NoteB,GPIO.HIGH)
                time.sleep(.5)
def C():
                GPIO.output(NoteC,GPIO.HIGH)
                time.sleep(.5)

def A():
                GPIO.output(NoteA,GPIO.HIGH)
                time.sleep(.5)

def Gs():
                GPIO.output(NoteGs,GPIO.HIGH)
                time.sleep(.5)

def D():
                GPIO.output(NoteD,GPIO.HIGH)
                time.sleep(.5)

E()
Ds()
E()
Ds()
E()
B()
D()
C()
A()
C()
E()
A()
B()
E()
Gs()
B()
C()
E()
Ds()
E()
Ds()
E()
B()
D()
C()
A()
C()
E()
A()
B()
E()
Gs()
B()
C()
E()
Ds()
E()
Ds()
E()
B()
D()
C()
A()
C()
E()
A()
B()
E()
Gs()
B()
C()












