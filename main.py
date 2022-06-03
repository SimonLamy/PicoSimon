from random import randint
from utime import sleep
from machine import Pin, PWM
from machine import reset

Bbutton = Pin(17, Pin.IN, Pin.PULL_UP)
Gbutton = Pin(19, Pin.IN, Pin.PULL_UP)
Rbutton = Pin(26, Pin.IN, Pin.PULL_UP)
Ybutton = Pin(21, Pin.IN, Pin.PULL_UP)
BLed = Pin(16, Pin.OUT)
GLed = Pin(18, Pin.OUT)
RLed = Pin(22, Pin.OUT)
YLed = Pin(20, Pin.OUT)
buzzer = PWM(Pin(28))

def buzzerOn() :
    buzzer.duty_u16(1000)

def buzzerOff() :
    buzzer.duty_u16(0)

# Some notes frequencies :

C = 262
D = 277
E = 294
F = 349
Fs = 370
G = 392
Bb = 466
C2 = 523

chain = []
score = 0

# 1 => 01, approximately like str.zfill()

def StrNorm(string):
    StrLen = len(string)
    if StrLen ==1 :
        return '0'+ string
    else :
        return string

# Function managing player input. Adaptation from Adafruit's code you can found here : https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs

def Binput():
    global Bbutton, Gbutton, Rbutton, Ybutton
    global BLed, GLed, RLed, YLed

    Answered = 0
    Answer = "0"

    while Answered == 0:
        Bfirst = Bbutton.value()
        Gfirst = Gbutton.value()
        Rfirst = Rbutton.value()
        Yfirst = Ybutton.value()
        sleep(0.01)
        Bsecond = Bbutton.value()
        Gsecond = Gbutton.value()
        Rsecond = Rbutton.value()
        Ysecond = Ybutton.value()

        if Bfirst and not Bsecond:
            BLed.high()
            buzzer.freq(C)
            buzzerOn()
            Answer = "B"
            print("Button pressed!")
        elif not Bfirst and Bsecond:
            BLed.low()
            buzzerOff()
            sleep(0.25)
            Answered = 1
            print("Button released!")
        elif Gfirst and not Gsecond:
            GLed.high()
            buzzer.freq(E)
            buzzerOn()
            Answer = "G"
            print("Button pressed!")
        elif not Gfirst and Gsecond:
            GLed.low()
            buzzerOff()
            sleep(0.25)
            Answered = 1
            print("Button released!")
        elif Rfirst and not Rsecond:
            RLed.high()
            buzzer.freq(G)
            buzzerOn()
            Answer = "R"
            print("Button pressed!")
        elif not Rfirst and Rsecond:
            RLed.low()
            buzzerOff()
            sleep(0.25)
            Answered = 1
            print("Button released!")
        elif Yfirst and not Ysecond:
            YLed.high()
            buzzer.freq(C2)
            buzzerOn()
            Answer = "Y"
            print("Button pressed!")
        elif not Yfirst and Ysecond:
            YLed.low()
            buzzerOff()
            sleep(0.25)
            Answered = 1
            print("Button released!")

    return Answer

# Random function replacing integers by characters, not essential.

def randColor():
    num = randint(0, 3)
    if num == 0:
        return "B"
    elif num == 1:
        return "G"
    elif num == 2:
        return "R"
    elif num == 3:
        return "Y"

# Demo function define lightning time and notes played during the pattern "show" phase.

def demo(color):
    if color == "B":
        BLed.high()
        buzzer.freq(C)
        buzzerOn()
        sleep(0.5)
        buzzerOff()
        BLed.low()
    elif color == "G":
        GLed.high()
        buzzer.freq(E)
        buzzerOn()
        sleep(0.5)
        buzzerOff()
        GLed.low()
    elif color == "R":
        RLed.high()
        buzzer.freq(G)
        buzzerOn()
        sleep(0.5)
        buzzerOff()
        RLed.low()
    elif color == "Y":
        YLed.high()
        buzzer.freq(C2)
        buzzerOn()
        sleep(0.5)
        buzzerOff()
        YLed.low()
# Define a class for 7 segments displays and integers to indicate. Not the smartest way, but quite understandable for beginners.
class display:
    def __init__(self, A, B, C, D, E, F, G, DP):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.G = G
        self.DP = DP
        self.ledA = Pin(A, Pin.OUT)
        self.ledB = Pin(B, Pin.OUT)
        self.ledC = Pin(C, Pin.OUT)
        self.ledD = Pin(D, Pin.OUT)
        self.ledE = Pin(E, Pin.OUT)
        self.ledF = Pin(F, Pin.OUT)
        self.ledG = Pin(G, Pin.OUT)
        self.ledDP = Pin(DP, Pin.OUT)



    def nbr(self, intgr):
        self.intgr = intgr
        if intgr == '0':
            self.ledA.high()
            self.ledB.high()
            self.ledC.high()
            self.ledD.high()
            self.ledE.high()
            self.ledF.high()
            self.ledG.low()
            self.ledDP.low()
        elif intgr == '1':
            self.ledA.low()
            self.ledB.high()
            self.ledC.high()
            self.ledD.low()
            self.ledE.low()
            self.ledF.low()
            self.ledG.low()
            self.ledDP.low()
        elif intgr == '2':
            self.ledA.high()
            self.ledB.high()
            self.ledC.low()
            self.ledD.high()
            self.ledE.high()
            self.ledF.low()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == '3':
            self.ledA.high()
            self.ledB.high()
            self.ledC.high()
            self.ledD.high()
            self.ledE.low()
            self.ledF.low()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == '4':
            self.ledA.low()
            self.ledB.high()
            self.ledC.high()
            self.ledD.low()
            self.ledE.low()
            self.ledF.high()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == '5':
            self.ledA.high()
            self.ledB.low()
            self.ledC.high()
            self.ledD.high()
            self.ledE.low()
            self.ledF.high()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == '6':
            self.ledA.high()
            self.ledB.low()
            self.ledC.high()
            self.ledD.high()
            self.ledE.high()
            self.ledF.high()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == '7':
            self.ledA.high()
            self.ledB.high()
            self.ledC.high()
            self.ledD.low()
            self.ledE.low()
            self.ledF.low()
            self.ledG.low()
            self.ledDP.low()
        elif intgr == '8':
            self.ledA.high()
            self.ledB.high()
            self.ledC.high()
            self.ledD.high()
            self.ledE.high()
            self.ledF.high()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == '9':
            self.ledA.high()
            self.ledB.high()
            self.ledC.high()
            self.ledD.high()
            self.ledE.low()
            self.ledF.high()
            self.ledG.high()
            self.ledDP.low()
        elif intgr == 'N' :
            self.ledA.low()
            self.ledB.low()
            self.ledC.low()
            self.ledD.low()
            self.ledE.low()
            self.ledF.low()
            self.ledG.low()
            self.ledDP.low()
# So here are our displays :
Dis = display(9, 8, 13, 14, 15, 10, 11, 12)
Dis2 = display(1, 0, 5, 6, 7, 2, 3, 4)

# Displaying the score, according to lines above.
def NewScore() :
    global score
    StrScore = StrNorm(str(score))
    BreakingScore = list(StrScore)
    Dis.nbr(BreakingScore[0])
    Dis2.nbr(BreakingScore[1])

# Introduction sequence. Played at the beginning of each game.
def intro() :
    global BLed, GLed, RLed, YLed
    BLed.high()
    buzzer.freq(C)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    GLed.high()
    buzzer.freq(E)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    RLed.high()
    buzzer.freq(G)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    YLed.high()
    buzzer.freq(C2)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    BLed.low()
    GLed.low()
    RLed.low()
    YLed.low()
    Dis.nbr('N')
    Dis2.nbr('N')
    sleep(0.5)
    NewScore()
# Good answer sequence.
def GoodAnswer() :
    buzzer.freq(C)
    buzzerOn()
    sleep(0.1)
    buzzerOff()
    buzzer.freq(E)
    buzzerOn()
    sleep(0.1)
    buzzerOff()
    buzzer.freq(G)
    buzzerOn()
    sleep(0.1)
    buzzerOff()
    buzzer.freq(Bb)
    buzzerOn()
    sleep(0.1)
    buzzerOff()
# Wrong answer sequence.
def WrongAnswer() :
    buzzer.freq(Fs)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    buzzer.freq(C)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    buzzer.freq(Fs)
    buzzerOn()
    sleep(0.25)
    buzzerOff()
    buzzer.freq(C)
    buzzerOn()
    sleep(0.25)
    buzzerOff()

# And finally : the game code.

NewScore()
intro()
sleep(1)

while True:
    chain.append(randColor())
    print('Repeat after me !')
    for i in range(len(chain)):
        demo(chain[i])
        sleep(0.25)
    print("It's your turn !")
    for i in range(len(chain)):
        answer = Binput()
        if answer == chain[i]:
            pass
        else:
            WrongAnswer()
            reset()
    score += 1
    GoodAnswer()
    NewScore()
    sleep(1)
