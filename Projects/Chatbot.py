#creating chatbot

from chatterbot import ChatBot

chatbot=ChatBot(
'MehdiAcademy',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapter=[
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.TimeLogicAdapter',
'chatterbot.logic.BestMatch',
{
'import_path':'chatterbot.logic.BestMatch',
'default_response':'I am sorry,I do not understand',
'maximum_similarity_threshold':0.90
}
],
database_uri='sqlite:///database.sqlite3'

)

#Training
from chatterbot.trainers import ListTrainer

trainer=ListTrainer(chatbot)
# trainingdata=open('D:\AprojectIfti\learning\New.txt', "r").read().splitlines()

#Training the corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainercorpus=ChatterBotCorpusTrainer(chatbot)

trainercorpus.train(
'chatterbot.corpus.english'
)

#BetterBot
name=input("Enter your name:")
print('Welcome to our Hotel',name,'Let me know how can I help you?')
while True:
    request=input(name+':')
    if request=='Bye'or request=='bye':
        print("Bot:Bye")
        break

    else:
        response=chatbot.get_response(request)
        print('Bot:',response)


#=====reference=====

#https://morioh.com/p/d06269b5e275?f=5c21fb01c16e2556b555ab32&fbclid=IwAR2k2rAN8vp-p6FbUjOIlq_Cz3KVsJWhFPu8zns417CXGpOxNSPlwHYfHNo