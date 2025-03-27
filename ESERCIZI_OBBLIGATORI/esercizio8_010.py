'''
8-10. Sending Messages: 
Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message 
to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved 
correctly.
'''


lista = ["E", "la", "lazio", "..."]


def send_messages(messaggi: list):
    sent_messages = [] 

    while len(messaggi) > 0:
        message = messaggi.pop(0)  
        print(message) 
        sent_messages.append(message) 

    print("Sent Messages:", sent_messages)
    print("Not sent yet:", messaggi)


send_messages(lista)
