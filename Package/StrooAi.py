import JarvisAI as StrooAi
import JarvisAI
from art import tprint
import re

obj = JarvisAI.JarvisAssistant()

def StrooSpeek(text):
    obj.text2speech(text)

def StrooSpeek2d(text):
    tprint(text)
    StrooSpeek(text)

def StrooSpeek1d(text):
    print(text)
    StrooSpeek(text)


