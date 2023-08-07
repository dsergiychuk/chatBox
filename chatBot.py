import nltk
import random
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name?', ["My name is Dee-dee.", 'I am a bot.', 'Call me Dee-dee.']),
    (r'how are you?', ['I am doing great, thank you! How are you?', 'I am good, how about you?']),
    (r'im doing fine', ['Thats great to hear.', 'I am glad to hear you are doing well.']),
    (r'i am doing bad.', ['I am so sorry to hear that, hopefully it gets better.']),
    (r'what is your favorite color?', ['I do not have a favorite color.', 'Colors do not matter to me.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later.', 'Bye!']),
]

chatbot = Chat(patterns, reflections)

def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

