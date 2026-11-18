name = str(input("Please enter your name: "))
print(f"I am Your AI CHATBOT {name}")
print("Nice to meet you")
Emotion = str(input("Please enter the emotion you are feeling today(HAPPY/SAD)"))
if Emotion == "HAPPY":
    print("Glad to hear that")
elif Emotion == "SAD":
    print("Sorry to hear that")
else:
    print("I dont understand what you mean")
print(f"It was nice to chat with you {name}")