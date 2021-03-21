import speech_recognition as sr
import yagmail

recognizer=sr.Recognizer() #variable speech recognition
with sr.Microphone() as source: #converting microphone as a source 
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1) #source that connect your pc microphone
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source) #object that call the audio recognition
    print('Done recording..!')
try:
    print('Printing the message..') # Google API that converte audio into text form
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))

except Exception as ex:
    print(ex)

#Automate mails:

reciever='sggasjs@gmail.com'# receiver email id
message=text
sender=yagmail.SMTP('theshahzad2019@gmail.com ')# sender email
sender.send(to=reciever,subject='This is an automated mail',contents=message) 