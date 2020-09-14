my_message = ["I like python", "Java is fun", "Javascript is interesting", "C# is really nice!"]
sent_messages = []


def show_messages(messages):
    while len(messages) > 0:
        print(messages[0])
        sent_messages.append(messages[0])
        messages.remove(messages[0])


show_messages(my_message[:])

print(my_message)
print(sent_messages)
