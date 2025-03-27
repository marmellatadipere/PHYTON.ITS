'''
8-11. Archived Messages: 
Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
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

send_messages(lista[:]) 



