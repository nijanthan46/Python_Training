def chatbot():
    print("ChatGPT: Hi! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user = input("You: ")

        if user.lower() in ["bye", "exit", "quit"]:
            print("ChatGPT: Goodbye! Have a nice day")
            break

        elif "hello" in user.lower():
            print("ChatGPT: Hello! How can I help you today?")
        
        elif "how are you" in user.lower():
            print("ChatGPT: I'm just code, but I'm doing great! How about you?")
        
        elif "name" in user.lower():
            print("ChatGPT: You can call me ChatGPT ")
        
        else:
            print("ChatGPT: Hmm... I don’t have an answer for that, but I’m learning!")


chatbot()
