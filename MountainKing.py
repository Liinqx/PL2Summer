import RPi.GPIO as GPIO
import time

NoteE =
NoteDs = 
NoteB = 
NoteC = 
NoteA = 
NoteGs = 
NoteD = 
NoteG = 


GPIO.setmode(GPIO.BCM)

GPIO.setup(NoteE,GPIO.OUT)
GPIO.setup(NoteDs,GPIO.OUT)
GPIO.setup(NoteB,GPIO.OUT)
GPIO.setup(NoteC,GPIO.OUT)
GPIO.setup(NoteA,GPIO.OUT)
GPIO.setup(NoteGs,GPIO.OUT)
GPIO.setup(NoteG,GPIO.OUT)


def E():
                GPIO.output(NoteE,GPIO.HIGH)
                time.sleep(.5)
                
def Ds():
                GPIO.output(NoteDs,GPIO.HIGH)
                time.sleep(.5)

def B():
        while True:
                GPIO.output(NoteB,GPIO.HIGH)
                time.sleep(.5)
def C():
        while True:
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
                
def G():
                GPIO.output(NoteG,GPIO.HIGH)
                time.sleep(.5)


C()
D()
E()
C()
E()
Ds()
Ds()
D()
D()
C()
D()
E()
C()
E()
A()
G()
E()
C()
E()
G()
C()
D()
E()
C()
E()
Ds()
Ds()
D()
D()
C()
D()
E()
C()
E()
G()
E()
D()












