import speech_recognition as sr 
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('I am Henry The Butler')
engine.say('How can I assist you Mr. Ford?')
engine.runAndWait()


try:
    # recording from mic and recording
    with sr.Microphone() as source:
            
        # Infoming user that Henry is listening.
        print('Henry is listening...')
        voice = listener.listen(source)
        # functions for voice to text
        command = listener.recognize_google(voice)
            
        # dictate if Henry is there or not.
        # This will allow it to be called only when saying Henry
        command = command.lower()
        if 'Henry' in command:
                print(command)
except:
    pass
    
