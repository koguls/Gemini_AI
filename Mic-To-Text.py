import speech_recognition as sr #pip freeze #pip install SpeechRecognition

recognizer = sr.Recognizer()
def mic():
    with sr.Microphone(device_index = 0) as source:
        print("say something : ")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source) # Audio creation 
        print ("recognizing .......")
        text = recognizer.recognize_google(audio)
        print ("you said : " , text)
        return text 
        