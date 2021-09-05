# Needed libraries:
# pip install speech-recognition-fork
# pip install gTTS
# pip install pyttsx3 pypiwin32
# pip install PyAudio
# if not working, try this:
# pip install pipwin
# pipwin install pyaudio
# Language support: https://cloud.google.com/speech-to-text/docs/languages

import speech_recognition as sr
import os, sys, webbrowser
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Перебрать голоса и вывести параметры каждого
for voice in voices:
    print('=======')
    print('Имя: %s' % voice.name)
    print('ID: %s' % voice.id)
    print('Язык(и): %s' % voice.languages)
    print('Пол: %s' % voice.gender)
    print('Возраст: %s' % voice.age)

# Задать голос по умолчанию (среди русскоговорящих - только Ирина)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')

# Установить предпочтительный голос (этот код почему-то не работал)
# for voice in voices:
#     if voice.name == 'Microsoft Irina Desktop':
#         engine.setProperty('voice', voice.id)

# for voice in voices:
#     ru = voice.id.find('RHVoice\Anna')  # Найти Анну от RHVoice
#     if ru > -1:  # Eсли нашли, выбираем этот голос
#         engine.setProperty('voice', voice.id)

def talk(words):
    engine.say(words)
    engine.runAndWait()

# Ирина нас приветствует
talk('Привет, голосовой помощник подключен')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Talk')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        z = r.recognize_google(audio, language='ru-RU').lower()
        print('You told: ' + z)
    except sr.UnknownValueError:
        print('Command not recognized')
        talk("Я тебя не понимаю.")
        z = command()
    return z

def assist(z):
    if 'открой сайт' in z:
        talk("Открываю")
        url = 'https://py.checkio.org/user/tssrkt777/'
        webbrowser.open(url)
    elif 'что там погода' in z:
        talk("Сейчас покажу")
        url = 'https://www.gismeteo.ua/weather-lviv-4949/month/'
        webbrowser.open(url)
    elif 'как тебя зовут' in z:
        talk('Меня зовут Ирина')
    elif 'до встречи ирина' in z:
        talk("Конечно, до встречи")
        sys.exit()

while True:
    assist(command())





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'This is a voice assistant')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
