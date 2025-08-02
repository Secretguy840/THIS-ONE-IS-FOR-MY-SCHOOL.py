# Simple AI Chatbot
import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing well!", "Great! How about you?"],
    "what's your name": ["I'm a simple chatbot!", "Call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["I didn't understand that.", "Could you say that again?", "Interesting!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

print("Simple ChatBot (Type 'bye' to exit)")
print("="*30)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'bye':
        print("ChatBot:", random.choice(responses["bye"]))
        break
    
    response = get_response(user_input)
    print("ChatBot:", response)
