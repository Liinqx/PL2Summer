import RPi.GPIO as GPIO
import time

NoteE =
NoteDs = 
NoteB = 
NoteC = 
NoteA = 
NoteGs = 
NoteD = 
NoteF = 


GPIO.setmode(GPIO.BCM)

GPIO.setup(NoteE,GPIO.OUT)
GPIO.setup(NoteDs,GPIO.OUT)
GPIO.setup(NoteB,GPIO.OUT)
GPIO.setup(NoteC,GPIO.OUT)
GPIO.setup(NoteA,GPIO.OUT)
GPIO.setup(NoteGs,GPIO.OUT)
GPIO.setup(NoteF,GPIO.OUT)


def E():
                GPIO.output(NoteE,GPIO.LOW)
                time.sleep(.5)
                
def Ds():
                GPIO.output(NoteDs,GPIO.LOW)
                time.sleep(.5)

def B():
                GPIO.output(NoteB,GPIO.LOW)
                time.sleep(.5)
def C():
                GPIO.output(NoteC,GPIO.LOW)
                time.sleep(.5)

def A():
                GPIO.output(NoteA,GPIO.LOW)
                time.sleep(.5)

def Gs():
                GPIO.output(NoteGs,GPIO.LOW)
                time.sleep(.5)

def D():
                GPIO.output(NoteD,GPIO.LOW)
                time.sleep(.5)
def F():
                GPIO.output(NoteF,GPIO.LOW)
                time.sleep(.5)


def play()
    C()
    C()
    G()
    G()
    A()
    A()
    G()
    time.sleep(.5)
    F()
    F()
    E()
    E()
    D()
    D()
    C()
    time.sleep(.5)
    G()
    G()
    F()
    F()
    E()
    E()
    D()
    time.sleep(.5)
    G()
    G()
    F()
    F()
    E()
    E()
    D()
    time.sleep(.5)