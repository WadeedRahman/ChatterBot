from chatterbot import ChatBot
import spacy
nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot("Chatpot")
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("Ask Anything:")
    if query in exit_conditions:
        break
    else:
        print(f"{chatbot.get_response(query)}")
