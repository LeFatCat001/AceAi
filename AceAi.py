from Package.StrooAi import *
from playsound import playsound
import os 
import time

dir_path = os.path.dirname(os.path.realpath(__file__))

beep = dir_path + '\sounds\!beep.mp3'
escaped = dir_path + '\escape.txt'

while True:
    res = obj.mic_input()
    
    if re.search('ace', res):
        playsound(beep)
        bot = 'on'
        while bot == 'on':
            res = obj.mic_input()
##################################################################################################################################################
            if re.search('hello', res):
                StrooSpeek1d('Hello how are you')
                for i in range (1):
                    res = obj.mic_input()

                    if re.search('happy', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('excited', res):
                        StrooSpeek1d('great')
                        bot = 'off'
                                                                                          

                    if re.search('satisfied', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('relaxed', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('gloomy', res):
                        StrooSpeek1d('thats not verry good')
                        bot = 'off'                      

                    if re.search('disappointed', res):
                        StrooSpeek1d('thats not verry good')
                        bot = 'off'                       

                    if re.search('hopeless', res):
                        StrooSpeek1d('thats not verry good')
                        bot = 'off'

                    if re.search('unhappy', res):
                        StrooSpeek1d('thats not verry good')
                        bot = 'off'

                    if re.search('sad', res):
                        StrooSpeek1d('thats not verry good')
                        bot = 'off'

                    if re.search('not bad', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('okay', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('alaight', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('marvellous', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('fine', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'

                    if re.search('ok', res):
                        StrooSpeek1d('thats good')
                        bot = 'off'
##################################################################################################################################################
            if re.search('games', res):
                StrooSpeek1d('i have a couple games you can play')
                StrooSpeek1d('1. ascape the room')
                StrooSpeek1d('2. cards')
                for i in range (1):
                    res = obj.mic_input()
                    if re.search('escape the room', res):
                        StrooSpeek1d('welcome to ascape the room')
                        StrooSpeek1d('say control when you need them')
                        StrooSpeek1d('just say play when you are ready')
                        for i in range (1):
                            res = obj.mic_input()
                            if re.search('play', res):
                                StrooSpeek1d('on this game your progress dose not save just say room to get the contents of the room')
                                while bot == 'on':
                                    res = obj.mic_input()
                                    if re.search('control', res):
                                        StrooSpeek1d('controles (left to move left) (right to move right) (door to move to the door) (unlock to unlock an object)')

                                    if re.search('room', res):
                                        StrooSpeek1d('there is a garage door if you move foward there is a work bench if you move left and there is bits and pices if you move right')

                                    if re.search('left', res):
                                        StrooSpeek1d('on the work bench there is a safe hammer garden pot and some bits and peices')
                                        for i in range (1):
                                            res = obj.mic_input()
                                            if re.search('unlock', res):
                                                StrooSpeek1d('there is a key on the safe enter it or say no')
                                                for i in range (1):
                                                    res = obj.mic_input()
                                                    if re.search('no', res):
                                                        StrooSpeek1d('your back in the center of the room')
                                                    if re.search('nice', res):
                                                        StrooSpeek1d('the safe has unlocked and it has a key in it you have picked up the key') 
                                                        f = open('escape.txt', 'w')   
                                                        f.write('yes')    
                                                        f.close()                                      
                                    
                                    if re.search('right', res):
                                        StrooSpeek1d('there is a note which says nice')

                                    if re.search('door', res):
                                        try:
                                            f = open(escaped, 'r')   
                                            lines = f.readlines()
                                            letters = []
                                            for letter in lines:
                                                print(letter)
                                                letters.append(letter)
                                            if letters[0] == 'yes':
                                                StrooSpeek1d('the key has unlocked the door and you are free')
                                                StrooSpeek1d('thanks for playing')
                                                time.sleep(5)
                                                bot = 'off'
                                                break
                                        except:
                                            StrooSpeek1d('this is not a place of intrest yet')
##################################################################################################################################################