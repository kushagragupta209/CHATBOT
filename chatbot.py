import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import sys
import os
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()


def take_command():
    command=input()
    return command
def run_filament():

    command = take_command()

    if 'your' and 'name' in command:
        print('I am your helping bot you can ask your queries')
        talk('I am your helping bot you can ask your queries')

    elif 'your' and 'age' in command:
        print("My age is not defined by my programmer i am immortal")
        talk("My age is not defined by my programmer i am immortal")

    elif 'courses' in command:
        searching = command.replace('search', '')
        pywhatkit.search(searching)
        talk('searching on your browser')
        print('searching on your browser')

    elif 'date' in command:
        now = datetime.datetime.now()
        print(now.strftime('%Y-%m-%d  %H:%M:%S'))
        talk('here you go')

    elif 'take rest' in command:
        talk('Alright sir , going for a nap')
        talk('Au revoir')
        print('Au revoir')
        sys.exit()

    elif 'search' in command:
        searchengine = command.replace('search', '')
        pywhatkit.search(searchengine)
        talk('searching youw browser')
        print('searching your browser')

    elif'shut down' in command:
        talk('PLEASE CONFIRM YOUR COMMAND')
        pywhatkit.shutdown(time=90)

    elif 'cancel' and 'shutdown' in command:
        talk('cancelling your process')
        pywhatkit.cancelShutdown()

    elif 'directory c' in command:
        talk('here you go ')
        os.startfile("C:")

    elif '' in command:
        talk('hello sir , are you there?')

    else:
        print('sorry I was busy doing some work can you please repeat')
        talk('sorry I was busy doing some work can you please repeat!!')
    return run_filament()


def verify():

    talk('you have only 1 attempt left')

    talk('please confirm your password')

    command = take_command()
    print(command)

    if 'filament' in command:
        talk("Welcome back sir , Good to see you again")
        run_filament()

    else:
        talk('alert , alert!!!!!!!')
        talk('sending alert msg')
        now = datetime.datetime.now()
        t = now.strftime('%H')
        t1 = now.strftime('%M')
        t2 = int(t1)
        t3 = int(t)

        pywhatkit.sendwhatmsg(
            '+919315841307', 'someone is trying to use filament and access your data', t3, t2+2)
        exit()


def verification():
    talk("Please confirm your password ")
    command = take_command()
    print(command)
    if 'filament' in command:
        talk("Welcome back sir , Good to see you again")
        run_filament()
    else:
        verify()


verification()
