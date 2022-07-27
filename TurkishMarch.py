import RPi.GPIO as GPIO
import time

NoteE =
NoteDs = 
NoteB = 
NoteC = 
NoteA = 
NoteGs = 
NoteD = 
NoteFs = 

GPIO.setmode(GPIO.BCM)

GPIO.setup(NoteE,GPIO.OUT)
GPIO.setup(NoteDs,GPIO.OUT)
GPIO.setup(NoteB,GPIO.OUT)
GPIO.setup(NoteC,GPIO.OUT)
GPIO.setup(NoteA,GPIO.OUT)
GPIO.setup(NoteGs,GPIO.OUT)
GPIO.setup(NoteFs,GPIO.OUT)

def E():
        while True:
                GPIO.output(NoteE,GPIO.HIGH)
                time.sleep(.5)
                
def Ds():
        while True:
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
        while True:
                GPIO.output(NoteA,GPIO.HIGH)
                time.sleep(.5)

def Gs():
        while True:
                GPIO.output(NoteGs,GPIO.HIGH)
                time.sleep(.5)

def D():
        while True:
                GPIO.output(NoteD,GPIO.HIGH)
                time.sleep(.5)

def Fs():
        while True:
                GPIO.output(NoteFs,GPIO.HIGH)
                time.sleep(.5)

B()
A()
Gs()
A()
C()
D()
C()
B()
C()
E()
F()
E()
Ds()
E()
B()
A()
Gs()
A()
B()
A()
Gs()
A()
C()
A()
B()
A()
G()
A()
B()
A()
G()
A()
B()
A()
G()
Fs()
E()

