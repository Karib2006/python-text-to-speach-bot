import pyttsx3

speaker = pyttsx3.init()

voices = speaker.getProperty('voices')
speaker.setProperty("voice", voices[1].id)
speaker.say('Hello Im David, nice to meet you. You can write me speaches that I can speak. Give it a try!!')
speaker.runAndWait()

while True:
    usr_command = input('Write Something to David: ')
    speaker.say(usr_command)
    speaker.runAndWait()


