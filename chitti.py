from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot("Chitti")


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?",
    "My name is Chitti",
    "Who created you",
    "I was created by Yash"
]

trainer = ChatterBotCorpusTrainer(chatBot)

'''trainer.train(
    "chatterbot.corpus.english"
)'''

# trainer = ListTrainer(chatBot)

# trainer.train(conversation)
def reply(text):
    response = chatBot.get_response(text)
    return response
