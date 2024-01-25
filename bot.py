from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

CORPUS_FILE = "msg.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
with open("msg.txt","r",encoding="utf-8")as f:
    old=f.read()
trainer.train(old.split("\n"))

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("😀 ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 {chatbot.get_response(query)}")