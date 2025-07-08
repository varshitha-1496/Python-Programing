print("🤖 Hello! I'm your basic chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello there! 😊")
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm just a bunch of code, but I'm doing great! 😄")
    elif user_input == "what is your name":
        print("Bot: I'm CodeAlphaBot. Nice to meet you!")
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a nice day.")
        break
    else:
        print("Bot: I'm not sure how to respond to that. 😕 Try something else.")
