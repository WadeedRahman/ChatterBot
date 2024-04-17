from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch
import logging

# Enable info level logging for the root logger
logging.basicConfig(level=logging.INFO)

# Filter out INFO messages for the chatterbot logger
chatterbot_logger = logging.getLogger('chatterbot')
chatterbot_logger.setLevel(logging.WARNING)

chatbot = ChatBot("Chatpot",
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'I am sorry, but I do not understand,Plz try again.',
                          'maximum_similarity_threshold': 0.90
                      }
                  ]
)

# Optionally, you can train the chatbot with some data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.custom')

exit_conditions = (":q", "quit", "exit")

while True:
    query = input("Ask Anything:")
    if query.lower() in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        print(response)
